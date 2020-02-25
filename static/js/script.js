$(document).ready(function(){
    console.log("Welcome to TryOn!");

    $("#login").submit(function(e){
        e.preventDefault();
        // alert("Logged In Now");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'auth/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log("data: "+data);
                window.location.href = data
            }
        });
    });

    $("#customer_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $("#shipper_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $("#vendor_register").submit(function(e){
        e.preventDefault();
        // alert("Customer Registered");
        var formdata = new FormData(this);
        // console.log("FormData: ");
        // for(var pair of formdata.entries()) {
        //     console.log(pair[0] + ', ' + pair[1]);
        // }
        $.ajax({
            url:'add/',
            type:'POST',
            processData: false,
            cache: false,
            contentType: false,
            data:formdata,
            success:function(data){
                console.log(data);
            }
        });
    });

    $('#v_doc, #s_doc').change(function(){
        // alert("File Selected");
        console.log(this);
    });

    $('#v_add, #s_add').change(function(){
        // alert("File Selected");
        console.log(this);
    });
});