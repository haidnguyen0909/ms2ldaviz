from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basicviz.models import UserExperiment, ExtraUsers, \
    MultiFileExperiment, MultiLink
from basicviz.constants import EXPERIMENT_STATUS_CODE

@login_required(login_url='/registration/login/')
def index(request):

    userexperiments = UserExperiment.objects.filter(user=request.user)
    experiments = []
    for ue in userexperiments:
        experiments.append(ue.experiment)

    exclude_individuals = []
    pending_individuals = []
    for experiment in experiments:

        # Remove those that are multi ones
        links = MultiLink.objects.filter(experiment=experiment)
        if len(links) > 0:
            exclude_individuals += [l.experiment for l in links]

        # Also exclude those with pending status
        pending_code, pending_msg = EXPERIMENT_STATUS_CODE[0]
        if experiment.status == pending_code:
            exclude_individuals.append(experiment)
            pending_individuals.append(experiment)

    show_pending = False if len(pending_individuals) == 0 else True
    for e in exclude_individuals:
        del experiments[experiments.index(e)]

    # retrieve the permission of experiments too
    experiments = list(set(experiments))
    permissions = []
    for e in experiments:
        ue = UserExperiment.objects.get(user = request.user,experiment = e)
        print experiment,ue.permission
        permissions.append(ue.permission)
    experiments = zip(experiments,permissions)

    context_dict = {'experiments': experiments}
    context_dict['user'] = request.user
    context_dict['pending_experiments'] = pending_individuals
    context_dict['show_pending'] = show_pending

    # to display additional links on the basicviz index page
    eu = ExtraUsers.objects.filter(user=request.user)
    if len(eu) > 0:
        extra_user = True
    else:
        extra_user = False
    context_dict['extra_user'] = extra_user

    mfe = MultiFileExperiment.objects.all()
    context_dict['mfe'] = mfe

    return render(request, 'basicviz/basicviz.html', context_dict)