from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Filma
from .models import Bozkatzailea


def hasieraketa():
    f1 = Filma(izenburua="Earthlings", zuzendaria="Shaun Monson", urtea="2005", generoa="DO", sinopsia="Using hidden cameras and never-before-seen footage, Earthlings chronicles the dayto-day practices of the largest industries in the world, all of which rely entirely on animals for profit.", bozkak="0")
    f2 = Filma(izenburua="The Herd", zuzendaria="Melanie Light", urtea="2014", generoa="TH", sinopsia="Imprisoned within inhuman squalor with other women. Paula's existence and human function is abused as a resource by her captors. Escape, on any level, is hopeless as the women are condemned to a life of enforced servitude at the whims of their imprisoners for one reason only - their milk.", bozkak="0")
    f3 = Filma(izenburua="Dominion", zuzendaria="Chris Delforce", urtea="2018", generoa="DO", sinopsia="Dominion uses drones, hidden and handheld cameras to expose the dark underbelly of modern animal agriculture, questioning the morality and validity of humankind's dominion over the animal kingdom. ", bozkak="0")
    f4 = Filma(izenburua="Matadero: lo que la industria cárnica esconde", zuzendaria="Aitor Garmendia", urtea="2017", generoa="DO", sinopsia="El trabajo que se presenta a continuación tiene como objetivo hacer visible la explotación y violencia sistemática que padecen los animales en mataderos, la cual es mantenida oculta de forma deliberada por la industria cárnica. Con esta investigación se aporta información relevante al actual debate social y político antiespecista promovido por el movimiento de derechos animales que exige la abolición de toda explotación animal. ", bozkak="0")
    f5 = Filma(izenburua="Gurean: animalien erabilera Euskal Herriko festetan", zuzendaria="Linas Korta", urtea="2018", generoa="DO", sinopsia="Askekintzak Euskal Herriko festetako animalien erabileraren inguruan inoiz egin den dokumentazio lan handiena bildu du. Gurean, 4 urteetan zehar (2014-2017) aktibista desberdinek ezkutuan grabatutako irudiekin osatutako dokumentala da.", bozkak="0")
    f6 = Filma(izenburua="Hiltegiak Euskal Herrian", zuzendaria="Nor", urtea="2018", generoa="DO", sinopsia="Azken minutua: Heriotza eta erresistentzia. 3 urteetan zehar Euskal Herriko edo inguruetako hiltegietan grabatutako irudiak dira honakoak.", bozkak="0")
    f7 = Filma(izenburua="Cowspiracy: The Sustainability Secret", zuzendaria="Kip Andersen eta Keegan Kuhn", urtea="2014", generoa="DO", sinopsia="Follow the shocking, yet humorous, journey of an aspiring environmentalist, as he daringly seeks to find the real solution to the most pressing environmental issues and true path to sustainability.", bozkak="0")
    f8 = Filma(izenburua="Munich 1962: isildu egia", zuzendaria="Larraitz Ariznabarreta eta Naroa Anabitarte", urtea="2014", generoa="DO", sinopsia="Kezka batetik sortutako proiektua da Munich 1962: isildu egia. Ordu hartan Munichen egon zirenen hitzak jaso dituzte Orreaga Taldeko kideek. Dokumental historikoa izateaz harago doa, ikus-entzulea hausnarketara gonbidatu nahi du. 'Iruditzen zaigu oraindik ere orduan gertatutakoak gaurkotasun handia duela; oraindik berdin jarraitzen dugu, garai hartan egin ziren akats berberak errepikatzen dira gaur egun', Naroa Anabitarte (Tolosa, 1979) Orreaga Taldeko kide eta dokumentalaren egilearen esanetan. Ez du ikusten politikarien aldetik akats berak ez errepikatzeko nahirik, 'ematen du dinamika beretan jarraitu nahi dela, aldez aurretik galduak diren bideak erabiliz'.", bozkak="0")
   
    f1.save()
    f2.save()
    f3.save()
    f4.save()
    f5.save()
    f6.save()
    f7.save()
    f8.save()


def index(request):
    if Filma.objects.filter().count() == 0:
        hasieraketa()
    return render(request, 'filmak/index.html')


def login(request):
    if request.method == "GET":
        return render(request, 'filmak/login.html')
    if 'log' in request.POST:
        erabiltzailea = request.POST['izena']
        pasahitza = request.POST['pasahitza']
        if(erabiltzailea == "" or pasahitza == ""):
            return render(request, 'filmak/login.html', {
                    'error_message': "Eremu guztiak bete behar dituzu.",
                })
        else:
            try: 
                user = authenticate(username=erabiltzailea, password=pasahitza)
                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        return render(request, 'filmak/homefilms.html' , {
                          'mezua': "Ongi etorri: " + erabiltzailea + "!"
                        })
                    else:
                        return render(request, 'filmak/login.html', {
                        'error_message': "Kontua desgaituta.",
                    })
                else:
                    return render(request, 'filmak/login.html', {
                        'error_message': "Login desegokia.",
                    })
            except Exception as e:
                 return render(request, 'filmak/login.html',{
                     'error_message': e,
                 })

def signup(request):
    if request.method == "GET":
        return render(request, 'filmak/signup.html')
    if(request.POST['izena']=="" or request.POST['pas']=="" or request.POST['pas2']==""):
         return render(request, 'filmak/signup.html', {
            'error_message': "Balio guztiak derrigorrezkoak dira.", 'erab_izena': request.POST['izena'],
        })
    elif (request.POST['pas']!=request.POST['pas2']):
         return render(request, 'filmak/signup.html', {
            'error_message': "Sartutako bi pasahitzak desberdinak dira.", 'erab_izena': request.POST['izena'],
        })
    else :
        try:
            User.objects.create_user(username=request.POST['izena'], email=None, password=request.POST['pas'])
            return render(request, 'filmak/login.html', {'error_message': "Ondo erregistratu zara " + request.POST['izena'] + ". Orain saioa has dezakezu."})
        except Exception as e:
            return render(request, 'filmak/signup.html',{
                          'error_message': "Errorea erreistratzerakoan. Agian jada erabiltzaile izen hori hartuta dago.",
                          })

def logout(request):
    auth_logout(request)
    return render(request, 'filmak/index.html')


@login_required(login_url='../../filmak/login')
def homefilms(request):
     return render(request, 'filmak/homefilms.html')


@login_required(login_url='../../filmak/login')
def filmakikusi(request):
    filmak = Filma.objects.all()
    paginator = Paginator(filmak, 4) # Show 4 films per page
    page = request.GET.get('page')
    try:
        filmak_orrian = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        filmak_orrian = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        filmak_orrian = paginator.page(paginator.num_pages)
    return render(request, 'filmak/filmakikusi.html', {'filmak': filmak_orrian})


@login_required(login_url='../../filmak/login')
def filmakbozkatu(request):
     if request.method == "GET":
        return render(request, 'filmak/filmakbozkatu.html', {'filmak': Filma.objects.all()})
     if 'bozkatu' in request.POST:
        filma = request.POST['filma']
        filmaObject = Filma.objects.get(izenburua=filma)

        if Bozkatzailea.objects.filter(erabiltzailea_id = request.user).exists():
             gogokoak = Bozkatzailea.objects.get(erabiltzailea_id = request.user).gogokofilmak
             if filmaObject in gogokoak.all():
                    return render(request, 'filmak/filmakbozkatu.html', {
                          'bozketa_ondo': filma + " dagoeneko bozkatu duzu" , 'filmak': Filma.objects.all()
                          })
             else: 
                 gogokoak.add(filmaObject)
        else:
            b1 = Bozkatzailea(erabiltzailea_id = request.user)
            b1.save()
            b1.gogokofilmak.add(filmaObject)
        filmaObject.bozkak +=1 
        filmaObject.save()
        return render(request, 'filmak/filmakbozkatu.html', {
                          'bozketa_ondo': "Bozketa ongi burutu da. Zure bozka: " + filma , 'filmak': Filma.objects.all()
                          })

@login_required(login_url='../../filmak/login')
def zaleak(request):
    if request.method == "GET":
        return render(request, 'filmak/zaleak.html', {'filmak': Filma.objects.all()})
    if "zaleakikusi" in request.POST:
       bozkatzaileak = Bozkatzailea.objects.all()
       bozkatzaileakArray = []
       for b in bozkatzaileak:
           if (b.gogokofilmak.filter(izenburua=request.POST['filma']).exists()):
               bozkatzaileakArray.append(b.erabiltzailea_id.username)
       filma = Filma.objects.get(izenburua=request.POST['filma'])
       return render(request, 'filmak/zaleak.html', {'filmak': Filma.objects.all(), 'aukera_filma': filma, 'bozkatzaileak': bozkatzaileakArray})