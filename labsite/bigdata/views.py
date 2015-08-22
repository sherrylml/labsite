from django.conf import settings
from django import http
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.http import is_safe_url
from django.utils.translation import LANGUAGE_SESSION_KEY, check_for_language
from .models.models import *
from .models.team_models import Professor, Postgraduate
from .models.Englishmodels import *
from .models.EnglishTeam_models import *


def index(request):
    '''
    首页
    '''
    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    news_list = News.objects.all().order_by('-time_stamp')
    if len(news_list) > 3:
        news_list = news_list[0:4]
    notices_list = Notices.objects.all().order_by('-time_stamp')
    if len(notices_list) > 3:
        notices_list = notices_list[0:4]
    meetings_list = Meetings.objects.all()
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    if len(Lab.objects.all()) > 0:
        lab_intro = Lab.objects.order_by('-id')[0].introduction
    else:
        lab_intro = "Please write the information about lab at first"

    language = 'zh'
    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = language

    return render(request, 'bigdata/index.html', locals())


def index_e(request):
    '''
    首页
    '''
    if len(Lab.objects.all()) > 0:
        if request.LANGUAGE_CODE == 'zh':
            lab_intro = Lab.objects.order_by('-id')[0].introduction
        else:
            lab_intro = LabEn.objects.order_by('-id')[0].introduction
    else:
        lab_intro = "Please write the information about lab at first"

    language = 'en'
    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = language

    return render(request, 'bigdata/index_e.html', locals())


def news(request):
    '''
    通知&新闻
    '''
    if request.LANGUAGE_CODE == 'zh':
        news_list = News.objects.order_by('-time_stamp')
        notices_list = Notices.objects.order_by('-time_stamp')
    else:
        news_list = NewsEn.objects.order_by('-time_stamp')
        notices_list = NoticesEn.objects.order_by('-time_stamp')

    return render_to_response('bigdata/news.html', locals(), RequestContext(request))


def news_detail(request, id):
    '''
    新闻详情
    '''
    item_id = int(id)

    if request.LANGUAGE_CODE == 'zh':
        size = News.objects.all().count() - 1
        first = News.objects.all()[0].id
        last = News.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not News.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not News.objects.filter(id=next_id).count():
                next_id += 1
        news = News.objects.get(id=item_id)
    else:
        size = NewsEn.objects.all().count() - 1
        first = NewsEn.objects.all()[0].id
        last = NewsEn.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not NewsEn.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not NewsEn.objects.filter(id=next_id).count():
                next_id += 1
        news = NewsEn.objects.get(id=item_id)

    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'news': news, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/news_detail.html', Context, RequestContext(request))


def notice_detail(request, id):
    '''
    通知详情
    '''
    item_id = int(id)

    if request.LANGUAGE_CODE == 'zh':
        size = Notices.objects.all().count() - 1
        first = Notices.objects.all()[0].id
        last = Notices.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not Notices.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not Notices.objects.filter(id=next_id).count():
                next_id += 1

        notice = Notices.objects.get(id=item_id)
    else:
        size = NoticesEn.objects.all().count() - 1
        first = NoticesEn.objects.all()[0].id
        last = NoticesEn.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not NoticesEn.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not NoticesEn.objects.filter(id=next_id).count():
                next_id += 1

        notice = NoticesEn.objects.get(id=item_id)

    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'notice': notice, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/notice_detail.html', Context, RequestContext(request))


def team(request):
    '''
    科研团队
    '''
    if request.LANGUAGE_CODE == 'zh':
        professors_list = Professor.objects.all()
        masters_list = Postgraduate.objects.filter(educational_level='master')
        doctors_list = Postgraduate.objects.filter(educational_level='doctor')
    else:
        professors_list = ProfessorEn.objects.all()
        masters_list = PostgraduateEn.objects.filter(educational_level='master')
        doctors_list = PostgraduateEn.objects.filter(educational_level='doctor')

    return render_to_response('bigdata/team.html', locals(), RequestContext(request))


def member_professor(request, id):
    '''
    个人主页
    '''
    item_id = int(id)

    if request.LANGUAGE_CODE == 'zh':
        member = Professor.objects.get(id=item_id)
        researchDir_list = member.resdir_set.all()
        workExp_list = member.workexp_set.all()
        patentPri_list = member.patpri_set.all()
        publishInf_list = member.pubinf_set.all()
        researchAct_list = member.resact_set.all()
    else:
        member = ProfessorEn.objects.get(id=item_id)
        researchDir_list = member.resdiren_set.all()
        workExp_list = member.workexpen_set.all()
        patentPri_list = member.patprien_set.all()
        publishInf_list = member.pubinfen_set.all()
        researchAct_list = member.resacten_set.all()

    return render_to_response('bigdata/member.html', locals(), RequestContext(request))


def member_postgraduate(request, id):
    '''
    个人主页
    '''
    item_id = int(id)

    if request.LANGUAGE_CODE == 'zh':
        member = Postgraduate.objects.get(id=item_id)
        researchDir_list = member.resdir1_set.all()
        workExp_list = member.workexp1_set.all()
        patentPri_list = member.patpri1_set.all()
        publishInf_list = member.pubinf1_set.all()
        researchAct_list = member.resact1_set.all()
    else:
        member = PostgraduateEn.objects.get(id=item_id)
        researchDir_list = member.resdir1en_set.all()
        workExp_list = member.workexp1en_set.all()
        patentPri_list = member.patpri1en_set.all()
        publishInf_list = member.pubinf1en_set.all()
        researchAct_list = member.resact1en_set.all()

    return render_to_response('bigdata/member.html', locals(), RequestContext(request))


class ResearchDirection():
    def __init__(self, direction, images):
        self.direction = direction
        self.images = images

def research(request):
    '''
    科学研究
    '''
    direction_list = []
    if len(Lab.objects.all()) > 0:
        if request.LANGUAGE_CODE == 'zh':
            research_directions = Lab.objects.order_by('-id')[0].directions_set.all()
            for research_direction in research_directions:
                direction_images = research_direction.images_set.all()
                direction_list.append(ResearchDirection(research_direction.research_direction, direction_images))
            research_achievement = Lab.objects.order_by('-id')[0].achievement
        else:
            research_directions = LabEn.objects.order_by('-id')[0].directionsen_set.all()
            for research_direction in research_directions:
                direction_images = research_direction.imagesen_set.all()
                direction_list.append(ResearchDirection(research_direction.research_direction, direction_images))
            research_achievement = LabEn.objects.order_by('-id')[0].achievement
    else:
        research_achievement = " "
    Context = {'direction_list': direction_list, 'research_achievement': research_achievement}
    return render_to_response('bigdata/research.html', Context, RequestContext(request))

def publication(request):
    '''
    科学研究
    '''

    if len(Lab.objects.all()) > 0:
        if request.LANGUAGE_CODE == 'zh':
            research_achievement = Lab.objects.order_by('-id')[0].achievement
        else:
            research_achievement = LabEn.objects.order_by('-id')[0].achievement
    else:
        research_achievement = " "
    Context = {'research_achievement': research_achievement}
    return render_to_response('bigdata/publication.html', Context, RequestContext(request))

def academic(request):
    '''
    合作交流
    '''
    if request.LANGUAGE_CODE == 'zh':
        academic_list = Academic.objects.all()
        meetings_list = Meetings.objects.all()
    else:
        academic_list = AcademicEn.objects.all()
        meetings_list = MeetingsEn.objects.all()
    return render_to_response('bigdata/academic.html', locals(), RequestContext(request))


def academic_detail(request, id):
    '''
    学术交流活动详情
    '''
    item_id = int(id)

    if request.LANGUAGE_CODE == 'zh':
        size = Academic.objects.all().count() - 1
        first = Academic.objects.all()[0].id
        last = Academic.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not Academic.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not Academic.objects.filter(id=next_id).count():
                next_id += 1
        academic = Academic.objects.get(id=item_id)
    else:
        size = AcademicEn.objects.all().count() - 1
        first = AcademicEn.objects.all()[0].id
        last = AcademicEn.objects.all()[size].id

        if item_id == first:
            has_previous = False
            previous_id = item_id
        else:
            has_previous = True
            previous_id = item_id - 1
            while not AcademicEn.objects.filter(id=previous_id).count():
                previous_id -= 1

        if item_id == last:
            has_next = False
            next_id = item_id
        else:
            has_next = True
            next_id = item_id + 1
            while not AcademicEn.objects.filter(id=next_id).count():
                next_id += 1
        academic = AcademicEn.objects.get(id=item_id)

    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'academic': academic, 'Month': Month, 'has_previous': has_previous, 'has_next': has_next,
               'previous_id': previous_id, 'next_id': next_id}
    return render_to_response('bigdata/academic_detail.html', Context, RequestContext(request))

def relax(request, id):
    '''
    活动休闲
    '''
    curr_page = int(id)

    if request.LANGUAGE_CODE == 'zh':
        size = Relax.objects.all().count()
        if size % 5 == 0:
            all_page = size // 5
        else:
            all_page = size // 5 + 1
        start_pos = (curr_page - 1) * 5
        end_pos = start_pos + 5
        if size < end_pos:
            end_pos = size
        if curr_page == 1:
            has_previous = False
        else:
            has_previous = True
        if curr_page == all_page or size == 0:
            has_next = False
        else:
            has_next = True
        previous_page = curr_page - 1
        next_page = curr_page + 1
        relax_list = Relax.objects.all()[start_pos: end_pos]
    else:
        size = RelaxEn.objects.all().count()
        if size % 5 == 0:
            all_page = size // 5
        else:
            all_page = size // 5 + 1
        start_pos = (curr_page - 1) * 5
        end_pos = start_pos + 5
        if size < end_pos:
            end_pos = size
        if curr_page == 1:
            has_previous = False
        else:
            has_previous = True
        if curr_page == all_page or size == 0:
            has_next = False
        else:
            has_next = True
        previous_page = curr_page - 1
        next_page = curr_page + 1
        relax_list = RelaxEn.objects.all()[start_pos: end_pos]

    Month = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
             11: 'NOV', 12: 'DEC'}
    Context = {'relax_list': relax_list, 'Month': Month, 'has_next': has_next, 'has_previous': has_previous,
               'previous_page': previous_page, 'next_page': next_page}
    return render(request, 'bigdata/relax.html', Context)


def join(request):
    '''
    加入我们
    '''
    if request.LANGUAGE_CODE == 'zh':
        join1_list = Join1.objects.order_by('-time_stamp')
        join2_list = Join2.objects.order_by('-time_stamp')
    else:
        join1_list = Join1En.objects.order_by('-time_stamp')
        join2_list = Join2En.objects.order_by('-time_stamp')
    return render(request, 'bigdata/join.html', locals())


def about(request):
    '''
    关于
    '''
    if len(Lab.objects.all()) > 0:
        if request.LANGUAGE_CODE == 'zh':
            lab_intro = Lab.objects.order_by('-id')[0].introduction
        else:
            lab_intro = LabEn.objects.order_by('-id')[0].introduction
    else:
        lab_intro = "Please write the information about lab at first"
    Context = {'lab_intro': lab_intro}
    return render(request, 'bigdata/about.html', Context)

def changeHomepage(request):
    '''
    首页中英文交替
    '''
    # next = request.POST.get('next', request.GET.get('next'))
    # if not is_safe_url(url=next, host=request.get_host()):
    #     next = request.META.get('HTTP_REFERER')
    #     if not is_safe_url(url=next, host=request.get_host()):
    #         next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'POST':
        language = request.POST.get('language', None)

        if language and check_for_language(language):
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = language
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language,
                                    max_age=settings.LANGUAGE_COOKIE_AGE,
                                    path=settings.LANGUAGE_COOKIE_PATH,
                                    domain=settings.LANGUAGE_COOKIE_DOMAIN)
            if language == 'zh':
                return HttpResponseRedirect('/chinesepage')
            else:
               return HttpResponseRedirect('/')

    elif request.LANGUAGE_CODE == 'zh':
        return HttpResponseRedirect('/chinesepage')

    else:
        return HttpResponseRedirect('/')


