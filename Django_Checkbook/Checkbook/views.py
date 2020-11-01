from django.shortcuts import render


def home(request):
    return render(request, 'Checkbook/index.html')


def create_account(request):
    return render(request, 'Checkbook/CreateNewAccount.html')


def balance(request):
    return render(request, 'Checkbook/BalanceSheet.html')


def transaction(request):
    return render(request, 'Checkbook/AddTransaction.html')
