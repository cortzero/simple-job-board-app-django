from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.
def index(request):
  #jobs = JobPosting.objects.all()
  # jobs = JobPosting.objects.filter(is_active=False, company='Encora')
  # for job in jobs:
  #   print(f'TItle: {job.title}')
  #   print(f'Description: {job.description}')
  #   print(f'Company: {job.company}')
  #   print(f'Salary: {job.salary}')
  #   print(f'Active: {job.is_active}')
  #   print('-------------------------\n')
  active_postings = JobPosting.objects.filter(is_active=True)
  context = {
    'job_postings': active_postings
  }
  return render(request, 'job_board/index.html', context)

def job_details(request, id):
  job_posting = get_object_or_404(JobPosting, pk=id, is_active=True)
  context = {'job_posting': job_posting}
  return render(request, 'job_board/job_details.html', context)