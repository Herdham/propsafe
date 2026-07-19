from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignUpForm, LoginForm, SettingForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.messages import error
from .models import Profile
from django.db.models import Sum
from trading.models import Trade

User = get_user_model()

# Create your views here.

def home(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        login_form = LoginForm(request.POST)
        if "signup_btn" in request.POST:
            if form.is_valid():
                firstname = form.cleaned_data["firstname"]
                lastname = form.cleaned_data["lastname"]
                email = form.cleaned_data["email"]
                username = form.cleaned_data["username"]
                password1 = form.cleaned_data["password1"]

                user = User.objects.create(first_name=firstname, last_name=lastname, email=email, username=username, password=password1)
                user.set_password(password1)
                user.save()

                return redirect("account:login")
            return render(request, "authentication/signup.html", {"form": form})
        
        elif "login_btn" in request.POST:
            if login_form.is_valid():
                email = login_form.cleaned_data.get("email")
                password = login_form.cleaned_data.get("password")

                try:
                    user = User.objects.get(email=email)
                    user_auth = auth.authenticate(username=user.username, password=password)

                    if user_auth is not None:
                        auth.login(request, user_auth)
                        return redirect("trading:prop_dashboard")
                    else:
                        login_form.add_error("email", "User crendential is invalid check email or password")
                        return render(request, "authentication/login.html", {"login_form": login_form})
                    
                except User.DoesNotExist:
                    login_form.add_error("email", "User does not exist on this platform")
                    return render(request, "authentication/login.html", {"login_form": login_form})

            return render(request, "authentication/login.html", {"login_form": login_form})

        return render(request, "authentication/landing.html")
    else:
        return render(request, "authentication/landing.html")
    

def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get("email")
            password = login_form.cleaned_data.get("password")

            try:
                user = User.objects.get(email=email)
                user_auth = auth.authenticate(username=user.username, password=password)

                if user_auth is not None:
                    auth.login(request, user_auth)
                    return redirect("trading:prop_dashboard")
                else:
                    login_form.add_error("email", "User crendential is invalid check email or password")
                    return render(request, "authentication/login.html", {"login_form": login_form})
                
            except User.DoesNotExist:
                login_form.add_error("email", "User does not exist on this platform")
                return render(request, "authentication/login.html", {"login_form": login_form})

        return render(request, "authentication/login.html", {"login_form": login_form})
    return render(request, "authentication/login.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if "signup_btn" in request.POST:
            if form.is_valid():
                firstname = form.cleaned_data["firstname"]
                lastname = form.cleaned_data["lastname"]
                email = form.cleaned_data["email"]
                username = form.cleaned_data["username"]
                password1 = form.cleaned_data["password1"]

                user = User.objects.create(first_name=firstname, last_name=lastname, email=email, username=username, password=password1)
                user.set_password(password1)
                user.save()

                return redirect("account:login")
            return render(request, "authentication/signup.html", {"form": form})
    else:
        return render(request, "authentication/signup.html")


@login_required(login_url='login')
def profile(request, profile_id):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.select_related("user").get(user=user)
    total_trades = Trade.objects.filter(user=request.user).count()
    wining_trades = Trade.objects.filter(user=request.user, result="win").count()
    if total_trades > 0:
        win_rate = round((wining_trades / total_trades) * 100, 2)
    else:
        win_rate = 0
    context = {"user": user, "profile": profile, "total_trades": total_trades, "win_rate": win_rate}

    if request.method == 'POST':
        profile_picture = request.FILES.get("profilePicture")
        if profile_picture is not None:
            profile.profile_picture = profile_picture
            profile.save()
            return redirect("account:profile", profile_id)
        else:
            profile.profile_picture = profile.profile_picture
            profile.save()
            return redirect("account:profile", profile_id)
    else:
        return render(request, "dashboard/profile.html", context)


@login_required(login_url='login')
def setting(request, user_id):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=request.user)
    context = {"user": user, "profile": profile}
    if request.method == "POST":
        form = SettingForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            timezone = form.cleaned_data["timezone"]
            bio = form.cleaned_data["bio"]
            location = form.cleaned_data["location"]
            experience = form.cleaned_data["experience"]
            market = form.cleaned_data["market"]
            instrument = form.cleaned_data["instrument"]
            risk_per_trade = form.cleaned_data["risk_per_trade"]
            daily_goal = form.cleaned_data["daily_goal"]
            account_size = form.cleaned_data["account_size"]

            print(phone_number, timezone, bio, location, experience, market, instrument, risk_per_trade, daily_goal, account_size)

            profile.phone_number = phone_number
            profile.bio = bio
            profile.country = location
            profile.experience_level = experience
            profile.timezone = timezone
            profile.preferred_market = market
            profile.favourite_pair = instrument
            profile.account_size = account_size
            profile.risk_per_trade = risk_per_trade
            profile.daily_profit_target = daily_goal
            profile.save()

            return redirect("account:profile", profile.id)
        else:
            return render(request, "dashboard/settings.html", {"form": form})
    else:
        return render(request, "dashboard/settings.html", context)

#journal_option
def journal_option(request):
    if request.method == "POST":
        manual = request.POST.get("connection_type")
        mt5 = request.POST.get("connection_type")
        if mt5 == "mt5":
            return redirect("account:account_setup")
        else:
            return redirect("trading:prop_dashboard")
    else:
        return render(request, "authentication/journal_option.html")



#mt5_account setup
def mt5_account(request):
    return render(request, "authentication/mt5_account.html")


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('account:home')