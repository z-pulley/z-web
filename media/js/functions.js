$(document).ready(function() {
  // 4.A functionality from your instructions file
  $('.toggle-box h1').click(function() {//box title clic
    $(this).closest('.toggle-box').toggleClass('closed');
    $(this).next('div').slideToggle('fast');
    
    return false;
  });
  
  // 4.B functionality from your instructions file
  $('./* select-options */ a').click(function() {
    var p = $(this).closest('.toggle-box');
    
    $('a', p).removeClass('selected');
    $(this).addClass('selected');
    
    //p.toggleClass('closed');
    //p.find('div:first').slideToggle('fast');
    
    return false;
  });
  
  // 4.F functionality from your instructions file
  $('.toggle-all').click(function() {
    $(this).siblings().slideToggle('fast');
    $(this).toggleClass('closed');
    
    /*
    $('.toggle-box', p).addClass('closed');
    $('h1', p).next().slideUp('fast');
    */
    return false;
  });
  
  //clear the search input on focus
  $('.search-form .search-input input').focus(function() {
    if($(this).val() == $(this).get(0).defaultValue) {
      $(this).val("");
    }
  });
  
  //restore the search input on blur
  $('.search-form .search-input input').blur(function() {
    if($(this).val() == "") {
      $(this).val($(this).get(0).defaultValue);
    }
  });
  
  //map controls click
  $('.map-controls > li > a').click(function() {
    var p = $(this).closest('li');
    if(p.hasClass('active')) {
      p.removeClass('active');
      p.find('ul').slideUp('fast');
    } else {
      p.siblings('.active').removeClass('active').find('ul').slideUp('fast');
      
      p.toggleClass('active');
      p.find('ul').slideToggle('fast');
    }
    
    return false;
  });
  
  $('.see-more').click(function() {
    $(this).hide().next('.more-text').show();
    
    return false;
  });

  $('.basemap_type').click(function() {
          var p = $(this).parent().closest('li');
          if(p.hasClass('active')) {
              p.removeClass('active');
              p.find('ul').slideUp('fast');
          }
          this_id = $(this).attr('id');
          map.setBaseLayer(basemap_dict[this_id]);
      });


  $("a.download-window").click(function () {
	  var myhref = $(this).attr("href");
	  var newwin = window.open(myhref, "Downloading Data...",
				   "height=100,width=300,modal=yes,alwaysRaised=yes");
	  //newwin.document.write("<p>Downloading OpenOcean Data Now...</p>");
	  //newwin.location.href = myhref;
	  return false;
      });

//  $('a[id=downld-button]').click(function() {
//	  window.open("http://www.cnn.com");
//	  alert("Download Button");
//	  //$.get('http://neptune.mtoc.us/wcs?service=WCS&request=GetCoverage&version=1.1.0&identifier=NOS_Surveys.02000001&format=application/xyz&boundingbox=-8542331.06601,4426854.624536,-8401686.93399,4467213.375464,urn:ogc:def:crs:EPSG::900913', function(data) {
//	  //	  $('.result').html(data);
//	  //	  alert('Data Downloaded!');
//	  //    });
//  });


  var mapdiv = "main-map";
  if (pageid == "permalink") {
      mapdiv = "main-map-wide";
  }

  var wgs84_projection = new OpenLayers.Projection("EPSG:4326");
  var google_projection = new OpenLayers.Projection("EPSG:900913");

  map = new OpenLayers.Map(mapdiv, {
          controls: [new OpenLayers.Control.Navigation({zoomWheelEnabled : false}),
                     new OpenLayers.Control.ZoomPanel(),
                     new OpenLayers.Control.MousePosition()
                     ],
          projection: google_projection,
          displayProjection: wgs84_projection,
          units: "m",
          maxResolution: 156543.0339,
          maxExtent: new OpenLayers.Bounds(-20037508,-20037508,20037508,20037508.34),
          numZoomLevels:18,
          fallThrough: false  });

  var basemap_dict = [];
  basemap_dict['google_roads'] = new OpenLayers.Layer.Google("Google Roads",
                                                             {type: G_NORMAL_MAP, 'maxZoomLevel':18, 'sphericalMercator': true});
  map.addLayer(basemap_dict['google_roads']);

  basemap_dict['google_satellite'] = new OpenLayers.Layer.Google( "Google Satellite",
                                                                  {type: G_SATELLITE_MAP, 'maxZoomLevel':18, 'sphericalMercator': true});
  map.addLayer(basemap_dict['google_satellite']);

  basemap_dict['google_hybrid'] = new OpenLayers.Layer.Google( "Google Hybrid",
                                                               {type: G_HYBRID_MAP, 'maxZoomLevel':18, 'sphericalMercator': true});
  map.addLayer(basemap_dict['google_hybrid']);

  basemap_dict['google_terrain'] = new OpenLayers.Layer.Google( "Google Terrain",
                                                                {type: G_PHYSICAL_MAP, 'maxZoomLevel':18, 'sphericalMercator': true});
  map.addLayer(basemap_dict['google_terrain']);

  basemap_dict['osm'] = new OpenLayers.Layer.OSM("Open Street Maps");
  map.addLayer(basemap_dict['osm']);

  map.setBaseLayer(basemap_dict['google_hybrid']);

  //var bdb = new OpenLayers.Layer.WMS("BDB Test Layers",
  //				     //"http://bdb.mtoc.us:8080/spatialfusionserver/services/ows/wms/PI_WMS?",
  //				     //"http://hermes.mtoc.us:8088/cgi-bin/infinity?",
  //                                   "http://neptune.mtoc.us/cgi-bin/infinity?database=NOS_Surveys&",
  //				     {
  //					 transparent: 'TRUE',
  //					 layers: 'Boundaries_XXX'
  //				     },{
  //					 'reproject': false, 'isBaseLayer': false, 'visibility': true}
  //				     );
  //map.addLayer(bdb);
  //
  //map.addControl(new OpenLayers.Control.MousePosition({displayProjection: new OpenLayers.Projection("EPSG:4326")}));
  //
  //map.setCenter(new OpenLayers.LonLat(-13622000,6115000), 3);
});
