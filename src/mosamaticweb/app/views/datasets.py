from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.http import HttpResponseBadRequest
from django.conf import settings

from ..models.datasetmodel import DatasetModel


@method_decorator(login_required, name='dispatch')
class RetrieveDatasets(View):
    def get(self, request):
        datasets = DatasetModel.objects.filter(owner=request.user)
        return render(request, 'datasets.html', context={'datasets': datasets})
    

@method_decorator(login_required, name='dispatch')
class UploadAndCreateDataset(View):
    def post(self, request):
        # Process uploaded files
        file_paths = []
        file_names = []
        files = request.POST.getlist('files.path')
        if files is None or len(files) == 0:
            files = request.FILES.getlist('files')
            if files is None or len(files) == 0:
                return HttpResponseBadRequest('File upload without files in POST or FILES')
            else:
                for f in files:
                    if isinstance(f, TemporaryUploadedFile):
                        file_paths.append(f.temporary_file_path())
                        file_names.append(f.name)
                    elif isinstance(f, InMemoryUploadedFile):
                        file_path = default_storage.save('{}'.format(uuid.uuid4()), ContentFile(f.read()))
                        file_path = os.path.join(settings.MEDIA_ROOT, file_path)
                        file_paths.append(file_path)
                        file_names.append(f.name)
                    elif isinstance(f, str):
                        file_paths.append(f)
                        file_names.append(os.path.split(f)[1])
                    else:
                        return HttpResponseBadRequest('Unknown file type {}'.format(type(f)))
        else:
            file_paths = files
            file_names = request.POST.getlist('files.name')
        # Create new dataset and files
        dataset = DatasetModel.objects.create(name=)
        # Return all datasets
        datasets = DatasetModel.objects.filter(owner=request.user)
        return render(request, 'datasets.html', context={'datasets': datasets})