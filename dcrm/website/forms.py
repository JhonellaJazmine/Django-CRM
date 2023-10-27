from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record, Brand, Category, Product, User, Role


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'style': 'margin-right: 10px;'}),
        required=True
    )


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'roles')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'




# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "First Name", "class":"form-control"}), label ="")
    last_name = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "Last Name", "class":"form-control"}), label ="")
    email = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "Email", "class":"form-control"}), label ="")
    phone = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "Phone", "class":"form-control"}), label ="")
    address = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "Address", "class":"form-control"}), label ="")
    city = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "City", "class":"form-control"}), label ="")
    state = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "State", "class":"form-control"}), label ="")
    zipcode = forms.CharField(required =True, widget=forms.widgets.TextInput(attrs={'placeholder': "Zip Code", "class":"form-control"}), label ="")

    class Meta:
         model = Record
         exclude = ("user",)

class BrandForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Brand Name", "class": "form-control"}),
        label="")

    description = forms.CharField(
            required=False,  # You can set this as required or not based on your requirements
            widget=forms.Textarea(attrs={'placeholder': "Brand Description", "class": "form-control"}),
            label="Brand Description")
    
    image = forms.ImageField(
        required=False,
        label="Brand Image",
        widget=forms.FileInput(attrs={"class": "form-control-file"}),
        initial="image-svgrepo-com.svg"  # Set the default image here
)

    
    class Meta:
        model = Brand
        fields = ['name', 'description', 'image']

class AddCategoryForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Category Name", "class": "form-control"}),
        label="Category Name")

    description = forms.CharField(
        required=False,  # You can set this as required or not based on your requirements
        widget=forms.Textarea(attrs={'placeholder': "Category Description", "class": "form-control"}),
        label="Category Description")

    class Meta:
        model = Category
        fields = ['name', 'description']

class AddProductForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Product Name", "class": "form-control"}),
        label="Product Name")

    barcode = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': "Product Barcode", "class": "form-control"}),
        label="Product Barcode")

    price = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': "Product Price", "class": "form-control"}),
        label="Product Price")

    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'placeholder': "Product Description", "class": "form-control"}),
        label="Product Description")

    weight = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': "Product Weight", "class": "form-control"}),
        label="Product Weight")

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Product Category")

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Product Brand")

    stock_quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': "Product Stock Quantity", "class": "form-control"}),
        label="Product Stock Quantity")

    units_sold = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': "Product Units Sold", "class": "form-control"}),
        label="Product Units Sold")

    class Meta:
        model = Product
        fields = '__all__'

# class AddRoleForm(forms.ModelForm):
#     name = forms.CharField(
#         required=True,
#         widget=forms.TextInput(attrs={'placeholder': "Role Name", "class": "form-control"}),
#         label="")

#     class Meta:
#         model = Role
#         fields = ['name']
