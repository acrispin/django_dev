define([], function () {

    var AppRouter = Backbone.Router.extend({
        routes: {
            'logout': 'runLogout',
            '*actions': 'defaultAction' // default actions debe ir al ultimo siempre
        }
    });

    function emptyView() {
        $("#main").html('');
        $("#main").off(); // para evitar que no se repliquen eventos.
        request_ns.showLoading();
        //$('.menu li').removeClass('active');
        //$('.menu li a[href="' + window.location.hash + '"]').parent().addClass('active');
        if ($('.navbar-collapse').hasClass('in')) {
            $('.navbar-collapse').collapse('hide');
        }
    }

    function renderView(view) {
        view.render();
        request_ns.hideLoading();
        $("html, body").scrollTop('0');
    }

    function resolveNode(params){
        var arr = [];
        var arr2 = [];
        var dict = {};
        var node = "";
        var rs = {"node":"home","dict":{}};

        if (typeof params == "string" && params !== "") {
            arr = params.split("?");
            if(arr.length > 1){
                node = arr[0];
                arr2 = arr[1].split("&");
                if(arr2.length > 1){
                    arr2.forEach(function(v,i){
                        dict[v.split("=")[0]] = v.split("=")[1];
                    });
                }
                else {
                    arr2 = arr[1].split("/");
                    arr2.forEach(function(v,i){
                        dict["p"+(i+1)] = v;
                    });
                }
            }
            else {
                arr = params.split("/");
                node = arr.shift();
                arr.forEach(function(v,i){
                    dict["p"+(i+1)] = v;
                });
            }
            rs.node = node;
            rs.dict = dict;
            return rs;
        }
        else {
            return rs;
        }
    }

    // resolveNode();
    // resolveNode("home?p1=valor1&p2=valor2&p3=100&p4=456"); // 
    // resolveNode("home/valor1/valor2/100/456"); // mismo resultado que la sentencia anterior
    // resolveNode("home/test/otro?id=29239&nom=NombreValor&code=00192"); // con nombre de parametros
    // resolveNode("home/test/article?100/298/187"); // 3 parametros
    // resolveNode("home/test/article?/100/298/187"); // 4 parametros
    // resolveNode("report/material/stock"); // 2 parametros
    // resolveNode("report/material/stock?"); // sin parametros y con path compleja, es necesario el ? para que no tome "/material/stock" como parametros

    var pathNodes = {
        "home": "views/main/home",
        "article": "views/entities/article",
        "warehouse": "views/entities/warehouse",
        "reason": "views/entities/reason",
        "storageOrder": "views/process/storageOrder",
        "pickupOrder": "views/process/pickupOrder",
        "stock": "views/reports/stock",
        "kardex": "views/reports/kardex",
        "user": "views/security/user",
        "report/material/stock": "views/reports/stock"
    };

    var initialize = function () {

        var app_router = new AppRouter;
        var rs = {};
       
        // home
        app_router.on('route:defaultAction', function (params) {            
            // if(arguments[1] !== null){
            //     params = Array.prototype.join.call(arguments, '?');
            //     console.log(params);
            // }
            rs = resolveNode(location.hash.substr(1));
            try {
                emptyView();
                require([pathNodes[rs.node]], function (GenericView) {
                    if(typeof GenericView !== "function"){
                        request_ns.hideLoading();
                        main_ns.msgError("Error en carga de vista");
                        main_ns.renderTemplate("#main", "#error_template", []);
                        throw new Error("Error en cargar vista");
                        // throw "Error en cargar vista";
                    }
                    var _view = new GenericView(rs.dict);
                    renderView(_view);
                }, function (err) {
                    var failedId = err.requireModules && err.requireModules[0];
                    console.log(err.requireType);
                    console.log('modules: ' + err.requireModules);
                    requirejs.undef(failedId);
                    request_ns.clearLoading();
                    if (main_globals.flagDevelop) {
                        alert(err.requireType + "-" + failedId);
                    }
                    main_ns.renderTemplate("#main", "#error_template", []);
                });
            } catch (e) {
                console.log(e);
                main_ns.msgError("Sucedió un error inesperado.");
                request_ns.clearLoading();
                if (main_globals.flagDevelop) {
                    alert(e);
                }
            }
        });

        // salir de session
        app_router.on('route:runLogout', function () {
            try {
                console.log("implementar salir de session");
            } catch (e) {
                console.log(e);
                main_ns.msgError("Sucedió un error inesperado.");
                request_ns.clearLoading();
                if (main_globals.flagDevelop) {
                    alert(e);
                }
            }
        });
        
        Backbone.history.start();
    };

    return {
        initialize: initialize
    };

});
