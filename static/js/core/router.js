define([], function () {

    var AppRouter = Backbone.Router.extend({
        routes: {
            'logout': 'runLogout',
            '*actions': 'defaultAction' // default actions debe ir al ultimo siempre
        }
    });

    function emptyMain() {
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

    Backbone.View.prototype.close = function () {
        this.$el.empty().off();
        this.stopListening();
        if (this.onClose) {
            this.onClose();
        }
    }

    function AppView() {
        this.showView = function (view) {
            if (this.currentView) {
                this.currentView.close();
            }
            this.currentView = view;
            this.currentView.render();
            request_ns.hideLoading();
            $("html, body").scrollTop('0');
        };        
    }

    function resolveNode(params){
        var arr = [];
        var arr2 = [];
        var dict = {};
        var node = "";
        var rs = {"node":"","dict":{}};
        if (typeof params == "string" && params !== "") {
            arr = params.split("?");
            if(arr.length > 1){
                node = arr[0].split("/")[0];
                arr2 = arr[1].split("&");
                arr2.forEach(function(v,i){
                    dict[v.split("=")[0]] = v.split("=")[1];
                });
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
    // resolveNode("home?p1=shh&p2=122&p3=test");
    // resolveNode("home/test/8/78/uys");
    // resolveNode("home/test/8/78/uys?p1=shh&p2=122&p3=test");

    var mapNodes = {
        "home": "views/main/home",
        "article": "views/entities/article",
        "warehouse": "views/entities/warehouse",
        "reason": "views/entities/reason",
        "storageOrder": "views/process/storageOrder",
        "pickupOrder": "views/process/pickupOrder",
        "stock": "views/reports/stock",
        "kardex": "views/reports/kardex",
        "user": "views/security/user"
    };

    var initialize = function () {

        var app_router = new AppRouter;
        var app_view = new AppView;
        var rs = {};
       
        // home
        app_router.on('route:defaultAction', function (params) {
            rs_node = resolveNode(params);
            try {
                emptyMain();
                require([mapNodes[rs.node]], function (GenericView) {
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
