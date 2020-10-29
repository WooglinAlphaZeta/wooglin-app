from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from dashboard.models import Members, SoberBros, SoberBroSheets
from .forms import ProfileForm, SoberBroSignupForm
from django.urls import reverse_lazy
# from bootstrap_modal_forms.generic import BSModalCreateView
import datetime


# Create your views here.

@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    cur_user = Members.objects.get(email=request.user.email)

    form = ProfileForm(instance=cur_user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=cur_user)
        if form.is_valid():
            form.save()
        else:
            print("FORM INVALID")

    abroad = "Yes" if cur_user.abroad_flag else "No"
    inactive = "Yes" if cur_user.inactive_flag else "No"

    current_user = {
        "name": cur_user.name,
        "position": cur_user.position,
        "first_name": cur_user.name.split(" ")[0],
        "last_name": cur_user.name.split(" ")[1],
        "name": cur_user.name,
        "avatar": cur_user.avatar,
        "email": cur_user.email,
        "phone": cur_user.phone.replace(".", "-"),
        "address": cur_user.address,
        "rollnumber": cur_user.rollnumber,
        "member_score": cur_user.member_score,
        "present": cur_user.present,
        "abroad": abroad,
        "inactive": inactive,
        "legal_name": cur_user.legal_name
    }

    today = datetime.date.today()
    # sbsheets = get_sober_bro_sheets(today)
    # sober_bros = get_sober_brothers(today)

    perm_groups = request.user.groups.values_list('name', flat=True)
    perm_groups = set(perm_groups)

    brothers = Members.objects.all()

    return render(request,
                  'dashboard/dashboard.html',
                  {
                      'brothers': brothers,
                      'me': current_user,
                      'perms': perm_groups,
                      'form': form,
                      # 'sbsheets': sbsheets,
                      # 'sober_brothers': sober_bros,
                  }
                  )


# class SoberBroSignupCreateView(BSModalCreateView):
#     template_name = 'dashboard/editsbs.html'
#     form_class = SoberBroSignupForm
#     success_message = 'Success: Book was created.'
#     success_url = reverse_lazy('dashboard')


def get_sober_bro_sheets(today):
    sbsheets = SoberBroSheets.objects.exclude(
        start_date__gte=today
    ).filter(
        start_date__gte=datetime.date(today.year - 1, today.month, today.day)
    )

    return sbsheets


def get_sober_brothers(today):
    sober_bros = SoberBros.objects.exclude(
        date__gte=datetime.date(today.year, today.month, today.day + 1)
    ).filter(
        date__gte=datetime.date(today.year - 1, today.month, today.day)
    )

    return sober_bros
