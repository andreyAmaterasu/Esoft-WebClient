from django import forms
 
class TaskForm(forms.Form):
    taskname = forms.CharField(label='Наименование задачи', label_suffix='')
    aboutoftask = forms.CharField(label='Описание задачи', label_suffix='')
    periodofexecution = forms.DateField(label='Срок исполнения', label_suffix='')
    dateofcompletion = forms.DateField(label='Дата выполнения', label_suffix='')
    taskcomplexity = forms.IntegerField(label='Сложность задачи', label_suffix='')
    timetocompletethetask = forms.IntegerField(label='Время на выполнение задачи', label_suffix='')
    taskstatus = forms.CharField(label='Статус задачи', label_suffix='')
    natureofthetask = forms.CharField(label='Характер задачи', label_suffix='')
    taskperformer = forms.CharField(label='Исполнитель задачи', label_suffix='')
