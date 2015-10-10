define(['text!templates/main/home.html'],
function (homeTemplate) {

        var HomeView = Backbone.View.extend({
            el: $("#main"),
            initialize: function (params) {
                console.log(params);
                this.params = params;
            },
            template: Handlebars.compile(homeTemplate),
            render: function () {
                var html = this.template({ ListData: [] });
                this.$el.html(html);
            }
        });

        return HomeView;
    }
);