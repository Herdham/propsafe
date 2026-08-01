from django.shortcuts import render, redirect
from .models import Trade, TradeScreenShot
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max, Min
from account.models import Profile
from django.http import HttpResponse

User = get_user_model()

def new_trade(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    if request.method == "POST":
        instrument = request.POST.get("instrument")
        direction = request.POST.get("direction")
        market = request.POST.get("market")
        entry_price = request.POST.get("entry_price")
        exit_price = request.POST.get("exit_price")
        position_size = request.POST.get("position_size")
        leverage = request.POST.get("leverage")
        risk_per_trade = request.POST.get("risk_per_trade")
        account_size = request.POST.get("account_size")
        profit_and_loss = request.POST.get("profit_and_loss")
        profit_percent = request.POST.get("profit_percent")
        stop_loss = request.POST.get("stop_loss")
        take_profit = request.POST.get("take_profit")
        r_r = request.POST.get("risktoreward")
        risk_amount = request.POST.get("risk_amount")
        potential_reward = request.POST.get("potential_reward")
        expected_outcome = request.POST.get("expected_outcome")
        actual_outcome = request.POST.get("actual_outcome")
        status = request.POST.get("status")
        result = request.POST.get("result")
        setup = request.POST.get("setup")
        timeframe = request.POST.get("timeframe")
        session = request.POST.get("session")
        trade_note = request.POST.get("trade_note")
        date_time = request.POST.get("date_time")
        emotion_before = request.POST.get("emotion_before")
        emotion_during = request.POST.get("emotion_during")
        emotion_after = request.POST.get("emotion_after")
        trade_lesson = request.POST.get("trade_lesson")
        follow_plan = request.POST.get("follow_plan")
        confirmation = request.POST.get("confirmation")
        risk = request.POST.get("risk")
        revenge = request.POST.get("revenge")
        fomo = request.POST.get("fomo")
        news = request.POST.get("news")
        upload_file = request.POST.get("upload_file")
        caption = request.POST.get('caption')

        risk_amount = str(float(account_size) * (float(risk_per_trade) / 100))
        r_r = str((float(take_profit) - float(entry_price)) / (float(entry_price) - float(stop_loss)))

        if follow_plan == confirmation == fomo == risk == news == revenge == "true":
            follow_plan = confirmation = fomo = risk = news = revenge = True
            
            trade = Trade.objects.create(user=request.user, instrument=instrument, market=market, direction=direction, entry_price=entry_price, exit_price=exit_price, position_price=position_size, stop_loss=stop_loss, take_profit=take_profit, risk_per_trade=risk_per_trade, leverage=leverage, account_balance=account_size, profit_and_loss=profit_and_loss, profit_percent=profit_percent, risk_percent=r_r, risk_amount=risk_amount, potential_reward=potential_reward, expected_outcome=expected_outcome, actual_outcome=actual_outcome, status=status, result=result, setup=setup, timeframe=timeframe, session=session, entry_date=date_time, trade_notes=trade_note, emotion_before=emotion_before, emotion_during=emotion_during, emotion_after=emotion_after, lesson_learned=trade_lesson,followed_plan=follow_plan, followed_confirmation=confirmation, news_checked=news, risk_under_one_percent=risk, avoided_revenge_trade=revenge, avoided_fomo=fomo)
            trade.save()
            
            if upload_file:
                trade_screenshot = TradeScreenShot.objects.create(trade=trade, image=upload_file, caption=caption)
                trade_screenshot.save()
                return redirect("trading:trades")
            else:
                trade_screenshot = TradeScreenShot(trade=trade, caption=caption)
                trade_screenshot.save()
                return redirect("trading:trades")
        else:
            trade = Trade.objects.create(user=request.user, instrument=instrument, market=market, direction=direction, entry_price=entry_price, exit_price=exit_price, position_price=position_size, stop_loss=stop_loss, take_profit=take_profit, risk_per_trade=risk_per_trade, leverage=leverage, account_balance=account_size, profit_and_loss=profit_and_loss, profit_percent=profit_percent, risk_percent=r_r, risk_amount=risk_amount, potential_reward=potential_reward, expected_outcome=expected_outcome, actual_outcome=actual_outcome, status=status, result=result, setup=setup, timeframe=timeframe, session=session, entry_date=date_time, trade_notes=trade_note, emotion_before=emotion_before, emotion_during=emotion_during, emotion_after=emotion_after, lesson_learned=trade_lesson)
            trade.save()
            
            if upload_file:
                trade_screenshot = TradeScreenShot.objects.create(trade=trade, image=upload_file, caption=caption)
                trade_screenshot.save()
                return redirect("trading:trades")
            else:
                trade_screenshot = TradeScreenShot(trade=trade, caption=caption)
                trade_screenshot.save()
                return redirect("trading:trades")
        
    else:
        return render(request, "dashboard/new_trade.html", context)


def trades(request):
    profile = Profile.objects.get(user=request.user)
    trades = Trade.objects.filter(user=request.user)
    total_trades = Trade.objects.filter(user=request.user).count()
    wining_trades = Trade.objects.filter(user=request.user, result="win").count()
    losing_trades = Trade.objects.filter(user=request.user, result="loss").count()
    if total_trades > 0:
        win_rate = round((wining_trades / total_trades) * 100, 2)
    else:
        win_rate = 0
    net_pnl = Trade.objects.filter(user=request.user).aggregate(total=Sum("profit_and_loss"))
    forex = Trade.objects.filter(user=request.user, market="Forex").count()
    crypto = Trade.objects.filter(user=request.user, market="Crypto").count()
    indices = Trade.objects.filter(user=request.user, market="Indices").count()
    commodities = Trade.objects.filter(user=request.user, market="Commodities").count()

    context = {"trades": trades, "total_trades": total_trades, "win_rate": win_rate, "net_pnl": net_pnl, "wining_trades": wining_trades, "losing_trades": losing_trades, "forex": forex, "crypto": crypto, "indices": indices, "commodities": commodities, "profile": profile}
    return render(request, "dashboard/trades.html", context)


#dashboard
@login_required(login_url="")
def dashboard(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    user_trades = Trade.objects.filter(user=user)

    trades = user_trades[:5]
    total_trades = user_trades.count()
    winning_trades = user_trades.filter(result="win").count()
    losing_trades = user_trades.filter(result="loss").count()
    forex = user_trades.filter(market="Forex").count()
    crypto = user_trades.filter(market="Crypto").count()
    r_r = user_trades.aggregate(rr_sum=Sum("risk_per_trade"))

    # Safely extract total PnL from dictionary and default to 0 if None
    pnl_data = user_trades.aggregate(total=Sum("profit_and_loss"))
    net_pnl = pnl_data["total"] if pnl_data["total"] is not None else 0
    win_rate = round((winning_trades / total_trades) * 100, 2) if total_trades else 0
    loss_rate = round((losing_trades / total_trades) * 100, 2) if total_trades else 0
    average_rr = round((r_r["rr_sum"] / total_trades), 1) if total_trades else 0
    largest_win = user_trades.aggregate(largestWin=Max("profit_and_loss"))["largestWin"] if user_trades else 0
    largest_loss = user_trades.aggregate(largestLoss=Min("profit_and_loss"))["largestLoss"] if user_trades else 0

    context = {
        "user": user,
        "profile": profile,
        "trades": trades,
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
        "win_rate": win_rate,
        "loss_rate": loss_rate,
        "net_pnl": net_pnl,
        "average_rr": average_rr,
        "largest_win": largest_win,
        "largest_loss": largest_loss,
        "forex": forex,
        "crypto": crypto,
    }

    return render(request, "dashboard/home.html", context)