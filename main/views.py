from django.shortcuts import render

from main.models import Experience, Education


def show_main(request):
    context = {
        "name": "Mirza",
        "npm": "2506618572",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Ilmu Komputer di Fasilkom Universitas Indonesia dengan minat di bidang pengembangan software dan riset teknologi. Love code and design❤️."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Mirza",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Mirza",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)