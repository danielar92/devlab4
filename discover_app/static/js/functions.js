
            $( document ).ready(
                function() {
                    alert( "document loaded" );

                    $( "#sign_up" ).leanModal();

                    $("#siteloader").html('<object data="http://visual.ly/" />');
                   // $("#siteloader").html('<object data="https://system.netsuite.com/pages/customerlogin.jsp?country=US" />');

                    var $container = $('#container');
            
                    // initialize
                    $container.masonry({
                        columnWidth: 200,
                        itemSelector: '.item'
                    });

                    var msnry = $container.data('masonry');
    
                    $( "#text2" )
                        .mouseenter(
                            function() {
                                $(this).hide();
                                $("#text2_hover").show();
                            });

                    $( "#text2_hover" )
                        .mouseleave(
                            function() {
                                $(this).hide();
                                $("#text2").show();
                            });

                    $( "#text5" )
                        .mouseenter(
                            function() {
                                $(this).hide();
                                $("#text5_hover").show();
                            });

                    $( "#text5_hover" )
                        .mouseleave(
                            function() {
                                $(this).hide();
                                $("#text5").show();
                            })

                        .click(
                            function() {
                                $("#text6").fadeOut();
                                $("#wn_form").fadeIn();
                            });

                    $( "#sign_up" ).click(function() {
                        $( "#signup" ).fadeIn();
                    });

                    $( "#lean_overlay" ).click(function() {
                        $( "#signup" ).fadeOut();
                    });

                    $( ".modal_close" ).click(function() {
                        $( "#lean_overlay" ).fadeOut();
                        $( "#signup" ).fadeOut();
                    });

                });
