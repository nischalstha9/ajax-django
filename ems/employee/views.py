from django.shortcuts import render, get_object_or_404
from .models import Employee

from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import EmployeeForm

# Create your views here.

def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employee})

def save_employee_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employees = Employee.objects.all()
            data['html_employee_list'] = render_to_string('partial_employee_list.html', {
                'employees': employees
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    return save_employee_form(request, form, 'partial_employee_create.html')


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'partial_employee_update.html')

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        employees = Employee.objects.all()
        data['html_employee_list'] = render_to_string('partial_employee_list.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('partial_employee_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)