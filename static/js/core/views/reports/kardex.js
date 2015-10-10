define(['text!templates/reports/kardex.html'],
function (Template) {

        var KardexView = Backbone.View.extend({
            el: $("#main"),
            initialize: function (params) {
                console.log(params);
                this.params = params;
            },
            template: Handlebars.compile(Template),
            render: function () {
                var html = this.template({ ListData: [] });
                this.$el.html(html);
            }
        });

        return KardexView;
    }
);