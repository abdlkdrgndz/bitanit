/**
 * Created by PC on 16.9.2015.
 */
// T�M SAYFALARIN EFEKT �LE A�ILMASI
$(function () {
    $("html, body").fadeIn(220);
    $('[data-toggle="tooltip"]').tooltip() ;
    $('[data-toggle="popover"]').popover();
})


//F�LTRELEME ��LEM� VE BANNER FOTO�RAF DE����M�
  $(function () {
             $(".sale-label").click(function () {
                 var secilen = $(this).text();
                 // alert(secilen);
                 var yoket = $(".sirala").hide();
                 var goster =  $(".sirala:contains('" + secilen + "') ").fadeIn(600);


             })

      setInterval(function(){

          var sayi = Math.round(Math.random()*10);

          $(".banner").css({
              "transition" : "all 2s ease",
              "-webkit-transition" : "all 2s ease",
              "-moz-transition" : "all 2s ease",
              "background"  : "url(../../../media/images/slider/" + sayi + ".jpg) no-repeat",
              "background-size" : "cover"
                });

      }, 6000);



  })









