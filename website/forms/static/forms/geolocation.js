<script>
      // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.
	function Deg2Rad( deg ) {
	   return deg * Math.PI / 180;
     }

      var closest_road = function(lat,lng){
      	// call the api to get the array of all the alt lng with the road id.
      	// var array = [{lat:1231,lng:13213},{lat:123123,lng:123123}];
      	var dist=[];
      	for(var i=0;i<array.length;i++)
      	{
  			var x = Deg2Rad(lat)-Deg2Rad(array[i].lat);
      		var y = Deg2Rad(lng)-Deg2Rad(array[i].lng);
      		var d = x*x + y*y;
      		dist.push({"dist":d,"id":array[i].id});
      	}
      	dist.sort(function(a,b){
      		return a.dist-b.dist;
      	});
      	var top20 = dist.slice(0,20);
      	var unique = [];
      	unique.push({"id":top20[0].id,"cnt":1});
      	for(var j=1;j<top20.length;j++){
      		var chk = unique.indexOf(top20[i]);
      		if (chk == -1) 
      		{
      			unique.push({"id":top20[i].id,"cnt":1})
      		}
      		else
      		{
      			unique[chk].cnt++;
      		}
      	}
      }

      function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 6
        });
        var infoWindow = new google.maps.InfoWindow({map: map});

        // Try HTML5 geolocation.
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }
      }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
      }
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDOrUu1FXuJNQEpthSsCVNZ51-D8vqe9Fk&callback=initMap">
    </script>