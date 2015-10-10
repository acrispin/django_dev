define(['text!templates/entities/article.html'],
function (Template) {

        var ArticleView = Backbone.View.extend({
            el: $("#main"),
            initialize: function (params) {
                console.log(params);
                this.params = params;
            },
            template: Handlebars.compile(Template),
            render: function () {
                // var _this = this;
                // var input = {};
                // input.nropedido = _this.params.nroped;
                // input.nropropuesta = _this.params.nropro;
                // input.nroversion = _this.params.nrover;
                // try{
                //     request_ns.post_json('/data/marcas', input,
                //         function (data) {
                //             try {
                //                 var html = _this.template({ ListData: data });
                //                 _this.$el.html(html);
                //             } catch (e) {
                //                 console.log(e);
                //                 main_ns.msgError("Sucedió un error inesperado.");
                //             }
                //         }
                //     );
                // } catch(e) {
                //     console.log(e);
                //     main_ns.msgError("Sucedió un error inesperado.");
                // }
                var html = this.template({ ListData: [] });
                this.$el.html(html);
                // $('.username').text($("#hdnUserName").val());
            },
            events: {
                'click #btnCreate': 'openPopupCreate'
            },
            openPopupCreate: function (e) {            
                $("#pnlArticulo").modal("show");
            }
        });

        return ArticleView;
    }
);