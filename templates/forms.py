address = forms.CharField(
    label="Endereço",
    required=False,
    max_length=250,
    widget=forms.TextInput(
      attrs={
        "class": "form-control",
        "placeholder": "digite seu endereço"
      }
    )
  )



def clean_username(self):
    name - self.cleaned_data.get('username')

    if name:
        name = name.strip()
        if ' ' in name:
            raise forms.ValidationError("Não utilize espaços no nome do usuário.")
        elif not name.islower():
            raise forms.ValidationError("Nome de usuário não deve conter letras maiúsculas.")
        else:
            return name

def clean_password2(self):
    pass_1 = self.cleaned_data.get('password1')
    pass_2 = self.cleaned_data.get('password2')

    if pass_1 and pass_2:
        if pass_1 != pass_2:
            raise forms.ValidationError("As senhas não são iguais.")
        elif len(pass_2) < 8:
            raise forms.ValidationError("A senha deve conter pelo menos 8 caracteres.")
        elif pass_2.lower() == pass_2
            raise forms.ValidationError("A senha deve conter pelo menos um caractere maiúsculo.")
        elif pass_2.upper() == pass_2
            raise forms.ValidationError("A senha deve conter pelo menos um caractere minúsculo.")
        else:
            return pass_2

class Meta:
      model = CustomUser
      fields = ("username", "user_image", "email", "password1", "password2", "is_student", "is_teacher")

