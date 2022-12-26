# pylint: disable=missing-module-docstring
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from apps.cargo.models import CargoTb
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


@login_required
def cargo(request):
    print('veio pra essas view cargo')
    if request.method == 'GET':
        cargos = CargoTb.objects.all()
        paginator = Paginator(cargos, 8)
        page = request.GET.get('page')
        cargos_por_pagina = paginator.get_page(page)
        context = {
            "cargo": cargos,
            "paginacao": cargos_por_pagina,
        }
    return render(request, 'cargo.html', context)


@login_required
def cadastro(request):
    """Cadsatra um usuario no sistema."""
    if request.method == 'POST':
        desc = request.POST.get('Descricao')
        # nivel = request.POST.get('Nivel')
        nivel = "júnior"
        ativo = request.POST.get('ativo')
        usuario = request.user
        if ativo == 'on':
            ativo = True
        else:
            ativo = False

        if desc == '':
            print('chegou na if ')
            messages.error(request, 'O campo Descrição não pode ficar em branco.')
            return redirect('cadastro')

        if nivel == '':
            messages.error(request, 'O campo Nivel não pode ficar em branco.')
            return redirect('cadastro')

        try:
            print('entrou no try', desc, nivel, ativo, datetime.datetime.now(), usuario)
            newcargo = CargoTb(descricao=desc, nivel=nivel, status=ativo, dt_inclusao=datetime.datetime.now(),
                               usuario=usuario)
            newcargo.save()

            messages.success(request, 'Cargo cadastrado com sucesso.')

            return redirect('cadastro')
        except Exception:

            messages.error(request, 'Erro ao tentar cadastrar um cargo.')

            return redirect('cadastro')

    else:
        print('chegou no cadastro ')
        return render(request, 'cadastroCargo.html')


@login_required
def deleteCargo(request, id_cargo):
    print('chegou aqui no delete:')
    try:
        del_cargo = get_object_or_404(CargoTb, pk=id_cargo)
        print(del_cargo)
        del_cargo.delete()
        messages.success(request, 'Excluido com sucesso.')
        return redirect('cargo')
    except Exception:
        messages.error(request, 'Erro ao tentar deletar registro.')
        return render(request, 'cargo.html')


@login_required
def editarCargo(request, id_cargo):
    print('chegou aqui no edit:')
    if request.method == 'POST':
        try:
            desc = request.POST.get('Descricao')
            # nivel = request.POST.get('Nivel')
            nivel = "júnior"
            ativo = request.POST.get('ativo')
            usuario = request.user

            if ativo == 'on':
                ativo = True
            else:
                ativo = False

            print('chegou na view cadastro', desc is None)

            if desc == '':
                print('chegou na if ')
                messages.error(request, 'O campo Descrição não pode ficar em branco.')
                return redirect('cadastro')

            if nivel == '':
                messages.error(request, 'O campo Nivel não pode ficar em branco.')
                return redirect('cadastro')

            print('entrou no try', desc, nivel, ativo, datetime.datetime.now(), usuario)
            newcargo = CargoTb(descricao=desc, nivel=nivel, status=ativo, dt_inclusao=datetime.datetime.now(),
                               usuario=usuario)
            newcargo.save()

            # messages.success(request, 'Cargo cadastrado com sucesso.')

            return redirect('cargo')
        except Exception as e:
            return render(request, 'cargo.html')

    if request.method == 'GET':
        print('chegou no Get do editar')
        try:
            cargos = CargoTb.objects.get(id=id_cargo)
            context = {"cargo": cargos, }
            return render(request, 'editarCargo.html', context)

        except Exception:
            return render(request, 'cadastroCargo.html')
