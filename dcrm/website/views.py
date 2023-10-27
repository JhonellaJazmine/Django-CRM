from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, BrandForm, AddCategoryForm, AddProductForm
from .models import Record, Brand, Category, Product, User

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'user_list.html', {'users': users})

def home(request):
    record_count = count_records()
    brand_count = count_brands()
    product_count = count_products()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')

    else:
            return render(request, 'home.html', {'record_count': record_count, 'brand_count': brand_count, 'product_count': product_count})



# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()


            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered, Welcome!")
            return redirect('home')

    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect ('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
# def dashboard(request):
#     return render(request, 'dashboard.html')

def count_records():
    return Record.objects.count()

def count_brands():
    return Brand.objects.count()

def count_products():
    return Product.objects.count()

def dashboard(request):
    record_count = count_records()
    brand_count = count_brands()
    return render(request, 'home.html', {'record_count': record_count, 'brand_count': brand_count})

def customer(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'customer.html', {'records':records})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')
    
def category(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        return render(request, 'category.html', {'categories':categories})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

def brand(request):
    if request.user.is_authenticated:
        brands = Brand.objects.all()
        return render(request, 'brand.html', {'brands':brands})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

def edit_brand(request, brand_id):
    brand = Brand.objects.get (pk=brand_id)
   
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand')  # Redirect to the list of brands
    else:
        form = BrandForm(instance=brand)

    return render(request, 'edit_brand.html', {'form': form, 'brand': brand})

def add_brand(request):
    form = BrandForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            form = BrandForm(request.POST, request.FILES)  # Make sure to include request.FILES
            if form.is_valid():
                add_brand = form.save()
                messages.success(request, "Brand Added...")
                return redirect ('brand')
        return render(request, 'add_brand.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def view_brand(request, brand_id):
    # Retrieve the brand with the given ID from the database
    try:
        brand = Brand.objects.get(pk=brand_id)
        
    except Brand.DoesNotExist:
        # Handle the case where the brand does not exist
        return HttpResponse("Brand not found", status=404)

    # Render a template to display the brand details
    return render(request, 'view_brand.html', {'brand': brand})

def delete_brand(request, brand_id):
    # Retrieve the brand with the given ID from the database
    try:
        brand = Brand.objects.get(pk=brand_id)
    except Brand.DoesNotExist:
        # Handle the case where the brand does not exist
        return HttpResponse("Brand not found", status=404)

    # Perform the deletion (you can add additional confirmation logic here)
    brand.delete()
    messages.success(request, "Brand Deleted Successfully.")
    # Redirect to a page after the brand is deleted (e.g., the brand list page)
    return redirect('brand')  # Assuming 'brand' is the name of your brand list view

def add_category(request):
    form = AddCategoryForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_category = form.save()
                messages.success(request, "Category Added...")
                return redirect ('category')
        return render(request, 'add_category.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def view_category(request, category_id):
    # Retrieve the brand with the given ID from the database
    try:
        category = Category.objects.get(pk=category_id)
        
    except category.DoesNotExist:
        # Handle the case where the category does not exist
        return HttpResponse("Category not found", status=404)

    # Render a template to display the category details
    return render(request, 'view_category.html', {'category': category})

def edit_category(request, category_id):
    category = Category.objects.get (pk=category_id)
   
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')  # Redirect to the list of brands
    else:
        form = AddCategoryForm(instance=category)

    return render(request, 'edit_category.html', {'form': form, 'category': category})


def delete_category(request, category_id):
    # Retrieve the category with the given ID from the database
    try:
        category = Category.objects.get(pk=category_id)
    except category.DoesNotExist:
        # Handle the case where the category does not exist
        return HttpResponse("Category not found", status=404)

    # Perform the deletion (you can add additional confirmation logic here)
    category.delete()
    messages.success(request, "Category Deleted Successfully.")
    # Redirect to a page after the category is deleted (e.g., the brand list page)
    return redirect('category')  # Assuming 'brand' is the name of your brand list view

def product(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        return render(request, 'product.html', {'products':products})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')

def add_product(request):
    form = AddProductForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method =="POST":
            if form.is_valid():
                add_product = form.save()
                messages.success(request, "Product Added...")
                return redirect ('product')
        return render(request, 'add_product.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
def view_product(request, product_id):
    # Retrieve the brand with the given ID from the database
    try:
        product = Product.objects.get(pk=product_id)
        
    except product.DoesNotExist:
        # Handle the case where the category does not exist
        return HttpResponse("Product not found", status=404)

    # Render a template to display the product details
    return render(request, 'view_product.html', {'product': product})

def edit_product(request, product_id):
    product = Product.objects.get (pk=product_id)
   
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated Successfully...")
            return redirect('product')  # Redirect to the list of product
    else:
        form = AddProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    # Retrieve the product with the given ID from the database
    try:
        product = Product.objects.get(pk=product_id)
    except product.DoesNotExist:
        # Handle the case where the product does not exist
        return HttpResponse("Product not found", status=404)

    # Perform the deletion (you can add additional confirmation logic here)
    product.delete()
    messages.success(request, "Product Deleted Successfully.")
    # Redirect to a page after the product is deleted (e.g., the product list page)
    return redirect('product')  # Assuming 'product' is the name of your product list view

# def add_role(request):
#     form = AddRoleForm(request.POST or None)
#     if request.user.is_authenticated:
#         if request.method =="POST":
#             if form.is_valid():
#                 add_role = form.save()
#                 messages.success(request, "Role Added...")
#                 return redirect ('home')
#         return render(request, 'add_role.html', {'form':form})
#     else:
#         messages.success(request, "You Must Be Logged In...")
#         return redirect('home')
    
def user(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'user.html', {'users':users})
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect('home')