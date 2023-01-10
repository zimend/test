from django.contrib.auth.models import User

def project_context(request):
    try:
        current_user = request.user
        context = {
            # 'the_hero' : User.objects.first()
            #'the_hero' : User.objects.get(username='rima')
            
            'the_hero' : User.objects.get(username=current_user)
        }
        return context
    except:
        context = {
                
            'the_hero' : None
        }
        return context
