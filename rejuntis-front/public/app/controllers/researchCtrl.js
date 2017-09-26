angular.module('researchControllers',['ui.bootstrap'])

.controller('resCtrl',function($scope,$http){
    
    $(document).ready(function() {
        $(".btn-pref .btn").click(function () {
            $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
            // $(".tab").addClass("active"); // instead of this do the below 
            $(this).removeClass("btn-default").addClass("btn-primary");   
        });
        });

    

    $scope.nomeDisciplinas = 'Lista de Disciplinas';

    $scope.listaDisciplinas = [];

    $scope.disciplina1 = {
                                "id":"calc1",
                                "nome":"Cálculo I",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };
            
    $scope.disciplina2 = {
                                "id":"algprog",
                                "nome":"Algoritmos e Programação",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };

    $scope.disciplina3 = {
                                "id":"epist",
                                "nome":"Epistemologia",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":30,
                                "creditos":"2",
                                "semestre":"1",
                                "isCollapsed":true
                            };
            
    $scope.disciplina4 = {
                                "id":"prodtext",
                                "nome":"Produção Textual",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };
    $scope.disciplina5 = {
                                "id":"alga",
                                "nome":"Álgebra Linear e Geometria Analítica",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };
            
    $scope.disciplina6 = {
                                "id":"logcomp",
                                "nome":"Lógica para Computação",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };

    $scope.disciplina7 = {
                                "id":"arq1",
                                "nome":"Arquitetura de Computadores I",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"1",
                                "isCollapsed":true
                            };
            
    $scope.disciplina8 = {
                                "id":"inteng",
                                "nome":"Introdução à Engenharia de Computação",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":30,
                                "creditos":"2",
                                "semestre":"1",
                                "isCollapsed":true
                            };
    
    $scope.disciplina9 = {
                                "id":"calc2",
                                "nome":"Cálculo II",
                                "prerequisito":"Cálculo I; Álgebra Linear e Geometria Analítica.",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"2",
                                "isCollapsed":true
                            };
    
    $scope.disciplina10 = {
                                "id":"estrdad",
                                "nome":"Estrutura de Dados",
                                "prerequisito":"Lógica para Computação; Algoritmos e Programação",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"2",
                                "isCollapsed":true
                            };

    $scope.disciplina11 = {
                                "id":"fis1",
                                "nome":"Física 1",
                                "prerequisito":"Cálculo I; Álgebra Linear e Geometria Analítica",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"2",
                                "isCollapsed":true
                            };

    $scope.disciplina12 = {
                                "id":"labfis1",
                                "nome":"Laboratório de Física 1",
                                "prerequisito":"Co-Requisito: Física I",
                                "cargahoraria":30,
                                "creditos":"2",
                                "semestre":"2",
                                "isCollapsed":true
                            };
    $scope.disciplina13 = {
                                "id":"tecdig",
                                "nome":"Técnicas Digitais",
                                "prerequisito":"Arquitetura de Computadores I",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"2",
                                "isCollapsed":true
                            };
    $scope.disciplina14 = {
                                "id":"arq2",
                                "nome":"Arquitetura de Computadores II",
                                "prerequisito":"Arquitetura de Computadores I",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"2",
                                "isCollapsed":true
                            };
            
    $scope.disciplina15 = {
                                "id":"metcient",
                                "nome":"Metodologia Científica",
                                "prerequisito":"Epistemologia",
                                "cargahoraria":30,
                                "creditos":"2",
                                "semestre":"2",
                                "isCollapsed":true
                            };

    $scope.disciplina16 = {
                                "id":"tecamb",
                                "nome":"Tecnologia, Ambiente e Sociedade",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":30,
                                "creditos":"2",
                                "semestre":"2",
                                "isCollapsed":true
                            };
    $scope.disciplina17 = {
                                "id":"bancodad",
                                "nome":"Banco de Dados",
                                "prerequisito":"Engenharia de Software",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };
    $scope.disciplina18 = {
                                "id":"compila",
                                "nome":"Compiladores",
                                "prerequisito":"Linguagens Formais e Gramáticas",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };
    $scope.disciplina19 = {
                                "id":"eduamb",
                                "nome":"Educação Ambiental e Sustentabilidade",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };
    $scope.disciplina20 = {
                                "id":"edudirhum",
                                "nome":"Educação, diversidade e direitos humanos",
                                "prerequisito":"Sem pré-requisitos",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };
    $scope.disciplina21 = {
                                "id":"gerredes",
                                "nome":"Gerência de Redes",
                                "prerequisito":"Redes de Computadores",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };
    $scope.disciplina22 = {
                                "id":"gestinov",
                                "nome":"Gestão da Inovação",
                                "prerequisito":"Gestão e Empreendedorismo",
                                "cargahoraria":60,
                                "creditos":"4",
                                "semestre":"e",
                                "isCollapsed":true
                            };

    $scope.listaDisciplinas.push($scope.disciplina1);
    $scope.listaDisciplinas.push($scope.disciplina2);
    $scope.listaDisciplinas.push($scope.disciplina3);
    $scope.listaDisciplinas.push($scope.disciplina4);
    $scope.listaDisciplinas.push($scope.disciplina5);
    $scope.listaDisciplinas.push($scope.disciplina6);
    $scope.listaDisciplinas.push($scope.disciplina7);
    $scope.listaDisciplinas.push($scope.disciplina8);
    $scope.listaDisciplinas.push($scope.disciplina9);
    $scope.listaDisciplinas.push($scope.disciplina10);
    $scope.listaDisciplinas.push($scope.disciplina11);
    $scope.listaDisciplinas.push($scope.disciplina12);
    $scope.listaDisciplinas.push($scope.disciplina13);
    $scope.listaDisciplinas.push($scope.disciplina14);
    $scope.listaDisciplinas.push($scope.disciplina15);
    $scope.listaDisciplinas.push($scope.disciplina16);
    $scope.listaDisciplinas.push($scope.disciplina17);
    $scope.listaDisciplinas.push($scope.disciplina18);
    $scope.listaDisciplinas.push($scope.disciplina19);
    $scope.listaDisciplinas.push($scope.disciplina20);
    $scope.listaDisciplinas.push($scope.disciplina21);
    $scope.listaDisciplinas.push($scope.disciplina22);

    $scope.selection = {
        ids: {"iduser": 102030}
    };
    this.resUser = function(resData){

    $http.post('/destination', function(req,res){
        //res.send('testing users route');
        res.json(req);
	});
        // app.loading = true;
        // app.errorMsg = false;
        // console.log('testing new thing');
        //console.log(this.regData);
        // User.create(app.regData).then(function(data){
        //     if(data.data.success){
        //         app.loading = false;
        //         app.successMsg = data.data.message;
        //         $timeout(function(){
        //             $location.path('/');
        //         },2000);
                
        //     }
        //     else{
        //         app.loading = false;
        //         app.errorMsg = data.data.message;
        //     }
        // });
   };
});