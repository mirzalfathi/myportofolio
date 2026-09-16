from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from main.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution_name",
            "level",
            "major",
            "description",
            "image",
            "start_year",
            "end_year",
        ]

        labels = {
            "institution_name": "Nama Institusi / Sekolah",
            "level": "Tingkat",
            "major": "Jurusan",
            "description": "Deskripsi",
            "image": "URL Foto",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Berakhir",
        }

        widgets = {
            "institution_name": TextInput(
                attrs={
                    "placeholder": "Universitas",
                    "maxlength": 255,
                }
            ),
            "level": TextInput(
                attrs={
                    "placeholder": "Tingkat",
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Sistem Informasi",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi studi",
                }
            ),
            "image": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2026",
                }
            ),
        }