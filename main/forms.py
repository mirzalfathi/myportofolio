from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from main.models import Education, Experience

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
                    "placeholder": "misal: Universitas Indonesia",
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
                    "placeholder": "misal: Sistem Informasi",
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
                    "placeholder": "misal: 2022",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "misal: 2026",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "Upload Thumbnail",
            "started_at": "Tahun Dimulai",
            "ended_at": "Tahun Berakhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "misal: OSIS MAN 4 Jakarta",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi pengalaman",
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "misal: full-time",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": NumberInput(
                attrs={
                    "placeholder": "misal: 2022",
                }
            ),
            "ended_at": NumberInput(
                attrs={
                    "placeholder": "misal: 2026",
                }
            ),
        }
