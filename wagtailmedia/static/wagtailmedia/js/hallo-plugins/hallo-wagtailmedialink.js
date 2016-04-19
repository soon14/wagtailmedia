// Generated by CoffeeScript 1.6.2
(function() {
    (function($) {
        return $.widget('IKS.hallowagtailmedialink', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var button, widget;

                widget = this;
                button = $('<span class="' + this.widgetName + '"></span>');
                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    label: 'Media',
                    // We can't use icon-media because Wagtail already have "Embed" with this icon
                    icon: 'icon-view',
                    command: null
                });
                toolbar.append(button);
                return button.on('click', function(event) {
                    var lastSelection;

                    lastSelection = widget.options.editable.getSelection();
                    return ModalWorkflow({
                        url: window.chooserUrls.mediaChooser,
                        responses: {
                            mediaChosen: function(mediaData) {
                                var a;

                                a = document.createElement('a');
                                a.setAttribute('href', mediaData.url);
                                a.setAttribute('data-id', mediaData.id);
                                a.setAttribute('data-linktype', 'media');
                                if ((!lastSelection.collapsed) && lastSelection.canSurroundContents()) {
                                    lastSelection.surroundContents(a);
                                } else {
                                    a.appendChild(document.createTextNode(mediaData.title));
                                    lastSelection.insertNode(a);
                                }

                                return widget.options.editable.element.trigger('change');
                            }
                        }
                    });
                });
            }
        });
    })(jQuery);

}).call(this);
