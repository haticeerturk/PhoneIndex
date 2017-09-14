from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Record
from .forms import RecordForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.postgres.search import SearchVector
from django.http import JsonResponse

def recordList(request):
	records = Record.objects.filter(registertime__lte=timezone.now()).order_by('registertime')
	return render(request, 'phone/recordList.html', {'records': records})

def recordDetail(request, pk):
	record = get_object_or_404(Record, pk=pk)
	return render(request, 'phone/recordDetail.html', {'record': record})

def recordNew(request):
	if request.method == "POST":
		form = RecordForm(request.POST)
		if form.is_valid():
			record = form.save(commit=False)
			record.user = request.user
			record.registertime = timezone.now()
			record.save()
			return redirect('recordDetail', pk = record.pk)
	else:
		form = RecordForm()
	return render(request, 'phone/recordEdit.html', {'form': form})

def recordEdit(request, pk):
	record = get_object_or_404(Record, pk=pk)
	if request.method == "POST":
		form = RecordForm(request.POST, instance=record)
		if form.is_valid():
			record = form.save(commit=False)
			record.user = request.user
			record.registertime = timezone.now()
			record.save()
			return redirect('recordDetail', pk=record.pk)
	else:
		form = RecordForm(instance=record)
	return render(request, 'phone/recordEdit.html', {'form': form})

def recordDelete(request, pk):
	record = get_object_or_404(Record, pk=pk)
	if request.method == "POST":
		record.delete()
		return redirect('recordList')

def recordSearch(request):
	print("geldimi")
	#data = Record.objects.filter(name=searchKey)
	data = 1
	print(data)
	return data