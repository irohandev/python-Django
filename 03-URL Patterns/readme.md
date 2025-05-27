
# Django URL Organization: App-Level URLs

## Problem

When copying Django apps between projects, you need to manually configure URLs in the main project file. This creates extra work and makes apps less reusable.

## Solution

Create `urls.py` files inside each app folder. This makes apps truly portable.

## Implementation

### Project Structure
```
myproject/
├── myproject/
│   ├── urls.py          # Main project URLs
│   └── settings.py
├── app1/
│   ├── views.py
│   ├── urls.py          # App1 URLs here
│   └── models.py
├── app2/
│   ├── views.py
│   ├── urls.py          # App2 URLs here
│   └── models.py
```

### App1 URLs
```python
# app1/urls.py
from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('/', views.detail, name='detail'),
]
```

### App2 URLs
```python
# app2/urls.py
from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]
```

### Main Project URLs
```python
# myproject/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
]
```

## Benefits

- **Easy Copy**: Just copy the app folder
- **No Extra Work**: URLs come with the app
- **Better Organization**: Each app manages its own URLs
- **Reusable**: Use the same app in multiple projects

## Copying Apps

1. Copy app folder to new project
2. Add app to `INSTALLED_APPS`
3. Include app URLs: `path('app1/', include('app1.urls'))`
4. Done!