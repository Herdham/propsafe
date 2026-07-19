const risk_per_trade = document.getElementById("riskpertrade")
const account_size = document.getElementById("account_size")
const risk_amount = document.getElementById("risk_amount")
const entry_price = document.getElementById("entry_price")
const exit_price = document.getElementById("exit_price")
const take_profit = document.getElementById("take_profit")
const stop_loss = document.getElementById("stop_loss")
const risk_to_reward = document.getElementById("risktoreward")
const buy_direction = document.getElementById("buy")
const sell_direction = document.getElementById("sell")
const position_size = document.getElementById("position_size")

function RiskAmountCalculator(){
    const riskPerTrade = parseFloat(risk_per_trade.value) || 0
    const accountSize = parseFloat(account_size.value) || 0

    if (!isNaN(riskPerTrade) && !isNaN(accountSize)) {
        risk_amount.value = accountSize * (riskPerTrade / 100)
    }
}

if (risk_per_trade && account_size) {  
    risk_per_trade.addEventListener("input", RiskAmountCalculator)
    account_size.addEventListener("input", RiskAmountCalculator)
}

if (buy_direction) {   
    buy_direction.addEventListener("click", (e) => {
        const direction_update = document.getElementById("direction_update")
        const r_r_update = document.getElementById("r_r_update")
        if (buy_direction.value == "buy") {  
            function RiskRewardCalculatorForBuy(){
                const entryPrice = parseFloat(entry_price.value) || 0
                const takeProfit = parseFloat(take_profit.value) || 0
                const stopLoss = parseFloat(stop_loss.value) || 0
            
                if (!isNaN(entryPrice) && !isNaN(takeProfit) && !isNaN(stopLoss)) {
                    const reward = takeProfit - entryPrice
                    const risk = entryPrice - stopLoss
                    const risk_reward = reward / risk
                    risk_to_reward.value = risk_reward
                    r_r_update.innerText = risk_reward
                }
            }
            
            take_profit.addEventListener("input", RiskRewardCalculatorForBuy)
            entry_price.addEventListener("input", RiskRewardCalculatorForBuy)
            stop_loss.addEventListener("input", RiskRewardCalculatorForBuy)

            direction_update.innerText = "Buy"
        }
    })
}

if(sell_direction){
    sell_direction.addEventListener("click", (e) => {
        const direction_update = document.getElementById("direction_update")
        const r_r_update = document.getElementById("r_r_update")
        if (sell_direction.value == "sell") {
            function RiskRewardCalculatorForSell(){
                const entryPrice = parseFloat(entry_price.value) || 0
                const takeProfit = parseFloat(take_profit.value) || 0
                const stopLoss = parseFloat(stop_loss.value) || 0
    
                if (!isNaN(entryPrice) && !isNaN(takeProfit) && !isNaN(stopLoss)) {
                    const reward = entryPrice - takeProfit
                    const risk = stopLoss - entryPrice
                    const risk_reward = reward / risk
                    risk_to_reward.value = risk_reward
                    r_r_update.innerText = risk_reward
                }
            }
    
            take_profit.addEventListener("input", RiskRewardCalculatorForSell)
            entry_price.addEventListener("input", RiskRewardCalculatorForSell)
            stop_loss.addEventListener("input", RiskRewardCalculatorForSell)
            
            direction_update.innerText = "Sell"
        }
    })
}


const account_balance = document.getElementById("account_balance")
const risk_percentage = document.getElementById("risk_percentage")
const risk_result = document.getElementById("risk_result")

function riskPercentageCalculator(){
    const accountBalance = parseFloat(account_balance.value) || 0
    const riskPercentage = parseFloat(risk_percentage.value) || 0

    if (!isNaN(accountBalance) && !isNaN(riskPercentage)) {
        const reward = accountBalance * (riskPercentage / 100)
        risk_result.innerText = `\$${reward}`
    }
}

if (account_balance && risk_per_trade) {
    account_balance.addEventListener("input", riskPercentageCalculator)
    risk_percentage.addEventListener("input", riskPercentageCalculator)
}

const accountSize = document.getElementById("account_size")
const profit_and_loss = document.getElementById("profit_and_loss")
const profit_percent = document.getElementById("profit_percent")

function ProfitPercent(){
    const accountBalance = parseFloat(accountSize.value) || 0
    const profitLoss = parseFloat(profit_and_loss.value) || 0

    if (!isNaN(accountBalance) && !isNaN(profitLoss)) {
        profit_percent.value = (profitLoss / accountBalance ) * 100
    }
}

if (accountSize && profit_and_loss) {
    accountSize.addEventListener("input", ProfitPercent)
    profit_and_loss.addEventListener("input", ProfitPercent)
}




const menu = document.querySelector(".first #menu")
const sideclose_btn = document.getElementById("sideclose_btn")
const sidebar_popup = document.querySelector(".sidebar_popup")

if (menu) {
    menu.addEventListener("click", (e) => {
        if (!sidebar_popup.classList.contains("modal_open")) {
            sidebar_popup.classList.add("modal_open")
            document.body.style.overflow = "hidden"
        }
    })
}

if (sideclose_btn) {
    sideclose_btn.addEventListener("click", (e) => {
        if (sidebar_popup.classList.contains("modal_open")) {
            sidebar_popup.classList.remove("modal_open")
            document.body.style.overflow = "auto"
        }
    })
}

const upload_file = document.querySelector(".upload_picture form input[type='file']")
const image_file_name = document.querySelector("#image_file_name")
if (upload_file) {
    upload_file.addEventListener("change", (e) => {
        const file = e.currentTarget.files[0]
        // image_file_name.innerText = file.name
        const image_url = URL.createObjectURL(file)
        const image_display = document.querySelector("form img")
        image_display.src = image_url
    })
}

const upload_picture_btn = document.getElementById("upload_picture_btn")
const uploadclose_btn = document.getElementById("uploadclose_btn")
const upload_picture = document.querySelector(".upload_picture")

if (upload_picture_btn) {
    upload_picture_btn.addEventListener("click", (e) => {
        if (!upload_picture.classList.contains("modal_open")) {
            upload_picture.classList.add("modal_open")
        }
    })
}

if (uploadclose_btn) {
    uploadclose_btn.addEventListener("click", (e) => {
        if (upload_picture.classList.contains("modal_open")) {
            upload_picture.classList.remove("modal_open")
        }
    })
}

const chart_one = document.getElementById("chart_one")
const chart_two = document.getElementById("chart_two")

if (chart_one) {
    const chartOne = new Chart(chart_one, {
        type: "doughnut",
        data: {
            labels: ['confident', 'Calm', 'Fearful', 'Frustrated', 'Other'],
            datasets: [{
                data: [20, 60, 50, 29, 33],
                backgroundColor: [
                    "rgba(54, 162, 235, 0.6)",
                    "rgba(255, 99, 132, 0.6)",
                    "rgba(255, 206, 86, 0.6)",
                    "rgba(75, 193, 192, 0.6)",
                    "rgba(153, 102, 255, 0.6)"
                ],
                label: "emotion_state"
            }]
        },
        options: {
            animation: true,
            maintainAspectRatio: false,
            cutout: "50%",
            radius: "90%",
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    })
}

if (chart_two) {
    const chartTwo = new Chart(chart_two, {
        type: "line",
        data: {
            labels: ["Jul 2", "Jul 8", "Jul 10", "Jul 18", "Jul 19", "Jul 22"],
            datasets: [{
                data: [20, 60, 50, 209, 33, 100, 80],
                borderColor: "#aa9faf",
                label: "performance"
            }]
        },
        options: {
            animation: true,
            maintainAspectRatio: false,
            elements:{
                line: {
                    tension: 1
                }   
            }
        }
    })
}

const entry_price_update = document.getElementById("entry_price_update")
if (entry_price_update) {   
    entry_price.addEventListener("input", (e) => {
        entry_price_update.innerText = entry_price.value
    })
}

const exit_price_update = document.getElementById("exit_price_update")
if (exit_price_update) {   
    exit_price.addEventListener("input", (e) => {
        exit_price_update.innerText = exit_price.value
    })
}

const position_update = document.getElementById("position_update")
if (position_update) {
    position_size.addEventListener("input", (e) => {
        position_update.innerText = position_size.value
    })
}



