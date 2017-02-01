from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=255,unique=True,null=False)
    update_link = models.CharField(max_length=255)
    download_date = models.DateField()

    def __str__(self):
        return self.country_name

class Shapefile(models.Model):
    country = models.ForeignKey(Country)
    filename = models.CharField(max_length=255,unique=True)
    driver = models.CharField(max_length=255)
    csr = models.CharField(max_length=255)
    schema = JSONField()
    geom = models.CharField(max_length=50)

    def __str__(self):
        return self.filename    
# select osm_id,'1001' as code,place as fclass,population,name,way from planet_osm_point where place='city' ;
# select osm_id,'1002' as code,place as fclass,population,name,way from planet_osm_point where place='town' ;
# select osm_id,'1003' as code,place as fclass,population,name,way from planet_osm_point where place='village' ;
# select osm_id,'1004' as code,place as fclass,population,name,way from planet_osm_point where place='hamlet' ;
# select osm_id,'1005' as code,'national_capital' as fclass,population,name,way from planet_osm_point where place='city' and (admin_level='2' or (capital='yes' and admin_level=null))  ;    
# select osm_id,'1010' as code,place as fclass,population,name,way from planet_osm_point where place='suburb' ;
# select osm_id,'1020' as code,place as fclass,population,name,way from planet_osm_point where place='island' ;
# select osm_id,'1030' as code,place as fclass,population,name,way from planet_osm_point where place='farm' ;
# select osm_id,'1031' as code,'dwelling' as fclass,population,name,way from planet_osm_point where place='isolated_dwelling' ;
# select osm_id,'1040' as code,place as fclass,population,name,way from planet_osm_point where place='region' ;
# select osm_id,'1041' as code,place as fclass,population,name,way from planet_osm_point where place='country' ;
# select osm_id,'1050' as code,place as fclass,population,name,way from planet_osm_point where place='locality' ;
class Places(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    population = models.IntegerField()
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()
    
    def __str__(self):
        return str(self.id)    

class Buildings(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    geom_multipolygon = models.MultiPolygonField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    
    
# select osm_id,'2001' as code,amenity as fclass,name,way from planet_osm_point where amenity='police' ;
# select osm_id,'2002' as code,amenity as fclass,name,way from planet_osm_point where amenity='fire_station' ;
# select osm_id,'2004' as code,amenity as fclass,name,way from planet_osm_point where amenity='post_box' ;
# select osm_id,'2005' as code,amenity as fclass,name,way from planet_osm_point where amenity='port_office' ;
# select osm_id,'2006' as code,amenity as fclass,name,way from planet_osm_point where amenity='telephone' ;
# select osm_id,'2007' as code,amenity as fclass,name,way from planet_osm_point where amenity='library' ;
# select osm_id,'2008' as code,amenity as fclass,name,way from planet_osm_point where amenity='townhall' ;
# select osm_id,'2009' as code,amenity as fclass,name,way from planet_osm_point where amenity='courthouse' ;
# select osm_id,'2010' as code,amenity as fclass,name,way from planet_osm_point where amenity='prison' ;
# select osm_id,'2011' as code,amenity as fclass,name,way from planet_osm_point where amenity='embassy' ;
# select osm_id,'2012' as code,amenity as fclass,name,way from planet_osm_point where amenity='community_centre' ;
# select osm_id,'2013' as code,amenity as fclass,name,way from planet_osm_point where amenity='nursing_home' ;
# select osm_id,'2014' as code,amenity as fclass,name,way from planet_osm_point where amenity='arts_centre' ;
# select osm_id,'2015' as code,'grave_yard' as fclass,name,way from planet_osm_point where amenity='grave_yard' or landuse='cemetry' ;
# select osm_id,'2016' as code,amenity as fclass,name,way from planet_osm_point where amenity='market_place' ;
# select osm_id,'2030' as code,amenity as fclass,name,way from planet_osm_point where amenity='recycling' ;
# select osm_id,'2081' as code,amenity as fclass,name,way from planet_osm_point where amenity='university' ;
# select osm_id,'2082' as code,amenity as fclass,name,way from planet_osm_point where amenity='school' ;
# select osm_id,'2083' as code,amenity as fclass,name,way from planet_osm_point where amenity='kindergarten' ;
# select osm_id,'2084' as code,amenity as fclass,name,way from planet_osm_point where amenity='college' ;
# select osm_id,'2099' as code,amenity as fclass,name,way from planet_osm_point where amenity='public_building' ;
# select osm_id,'2101' as code,amenity as fclass,name,way from planet_osm_point where amenity='pharmacy' ;
# select osm_id,'2110' as code,amenity as fclass,name,way from planet_osm_point where amenity='hospital' ;
# select osm_id,'2120' as code,amenity as fclass,name,way from planet_osm_point where amenity='doctors' ;
# select osm_id,'2121' as code,amenity as fclass,name,way from planet_osm_point where amenity='dentist' ;
# select osm_id,'2129' as code,amenity as fclass,name,way from planet_osm_point where amenity='veterinary' ;
# select osm_id,'2201' as code,amenity as fclass,name,way from planet_osm_point where amenity='theatre' ;
# select osm_id,'2202' as code,amenity as fclass,name,way from planet_osm_point where amenity='nightclub' ;
# select osm_id,'2203' as code,amenity as fclass,name,way from planet_osm_point where amenity='cinema' ;
# select osm_id,'2204' as code,leisure as fclass,name,way from planet_osm_point where leisure='park' ;
# select osm_id,'2205' as code,leisure as fclass,name,way from planet_osm_point where leisure='playground' ;
# select osm_id,'2206' as code,leisure as fclass,name,way from planet_osm_point where leisure='dog_park' ;
# select osm_id,'2251' as code,leisure as fclass,name,way from planet_osm_point where leisure='sports_centre' ;
# select osm_id,'2252' as code,leisure as fclass,name,way from planet_osm_point where leisure='pitch' ;
# select osm_id,'2253' as code,'swimming_pool' as fclass,name,way from planet_osm_point where amenity='swimming_pool' or leisure='swimming_pool' or sport='swimming' or leisure='water_park' ;
# select osm_id,'2254' as code,'tennis_court' as fclass,name,way from planet_osm_point where sport='tennis' ;
# select osm_id,'2255' as code,leisure as fclass,name,way from planet_osm_point where leisure='golf_course' ;
# select osm_id,'2256' as code,leisure as fclass,name,way from planet_osm_point where leisure='stadium' ;
# select osm_id,'2257' as code,leisure as fclass,name,way from planet_osm_point where leisure='ice_rink' ;
# select osm_id,'2301' as code,amenity as fclass,name,way from planet_osm_point where amenity='restaurant' ;
# select osm_id,'2302' as code,amenity as fclass,name,way from planet_osm_point where amenity='fast_food' ;
# select osm_id,'2303' as code,amenity as fclass,name,way from planet_osm_point where amenity='cafe' ;
# select osm_id,'2304' as code,amenity as fclass,name,way from planet_osm_point where amenity='pub' ;
# select osm_id,'2305' as code,amenity as fclass,name,way from planet_osm_point where amenity='bar' ;
# select osm_id,'2306' as code,amenity as fclass,name,way from planet_osm_point where amenity='food_court' ;
# select osm_id,'2307' as code,amenity as fclass,name,way from planet_osm_point where amenity='biergarten' ;
# select osm_id,'2401' as code,tourism as fclass,name,way from planet_osm_point where tourism='hotel' ;
# select osm_id,'2402' as code,tourism as fclass,name,way from planet_osm_point where tourism='motel' ;
# select osm_id,'2403' as code,tourism as fclass,name,way from planet_osm_point where tourism='bed_and_breakfast' ;
# select osm_id,'2404' as code,'guesthouse' as fclass,name,way from planet_osm_point where tourism='guest_house' ;
# select osm_id,'2405' as code,tourism as fclass,name,way from planet_osm_point where tourism='hostel' ;
# select osm_id,'2406' as code,tourism as fclass,name,way from planet_osm_point where tourism='chalet' ;
# select osm_id,'2421' as code,amenity as fclass,name,way from planet_osm_point where amenity='shelter' ;
# select osm_id,'2422' as code,tourism as fclass,name,way from planet_osm_point where tourism='camp_site' ;
# select osm_id,'2423' as code,tourism as fclass,name,way from planet_osm_point where tourism='alpine_hut' ;
# select osm_id,'2424' as code,tourism as fclass,name,way from planet_osm_point where tourism='caravan_site' ;
# select osm_id,'2501' as code,shop as fclass,name,way from planet_osm_point where shop='supermarket' ;
# select osm_id,'2502' as code,shop as fclass,name,way from planet_osm_point where shop='bakery' ;
# select osm_id,'2503' as code,shop as fclass,name,way from planet_osm_point where shop='kiosk' ;
# select osm_id,'2504' as code,shop as fclass,name,way from planet_osm_point where shop='mall' ;
# select osm_id,'2505' as code,shop as fclass,name,way from planet_osm_point where shop='department_store' ;
# select osm_id,'2511' as code,shop as fclass,name,way from planet_osm_point where shop='convenience' ;
# select osm_id,'2512' as code,shop as fclass,name,way from planet_osm_point where shop='clothes' ;
# select osm_id,'2513' as code,shop as fclass,name,way from planet_osm_point where shop='florist' ;
# select osm_id,'2514' as code,shop as fclass,name,way from planet_osm_point where shop='chemist' ;
# select osm_id,'2515' as code,shop as fclass,name,way from planet_osm_point where shop='books' ;
# select osm_id,'2516' as code,shop as fclass,name,way from planet_osm_point where shop='butcher' ;
# select osm_id,'2517' as code,'shoe_shop' as fclass,name,way from planet_osm_point where shop='shoes' ;
# select osm_id,'2518' as code,'beverages' as fclass,name,way from planet_osm_point where shop='alcohol' or shop='beverages';
# select osm_id,'2519' as code,shop as fclass,name,way from planet_osm_point where shop='optician' ;
# select osm_id,'2520' as code,'jeweller' as fclass,name,way from planet_osm_point where shop='jewelry' ;
# select osm_id,'2521' as code,'gift_shop' as fclass,name,way from planet_osm_point where shop='gift' ;
# select osm_id,'2522' as code,'sports_shop' as fclass,name,way from planet_osm_point where shop='sports' ;
# select osm_id,'2523' as code,shop as fclass,name,way from planet_osm_point where shop='stationery' ;
# select osm_id,'2524' as code,'outdoor_shop' as fclass,name,way from planet_osm_point where shop='outdoor' ;
# select osm_id,'2525' as code,'mobile_phone_shop' as fclass,name,way from planet_osm_point where shop='mobile_phone' ;
# select osm_id,'2526' as code,'toy_shop' as fclass,name,way from planet_osm_point where shop='toys' ;
# select osm_id,'2527' as code,shop as fclass,name,way from planet_osm_point where shop='newsagent' ;
# select osm_id,'2528' as code,shop as fclass,name,way from planet_osm_point where shop='greengrocer' ;
# select osm_id,'2529' as code,'beauty_shop' as fclass,name,way from planet_osm_point where shop='beauty' ;
# select osm_id,'2530' as code,'video_shop' as fclass,name,way from planet_osm_point where shop='video' ;
# select osm_id,'2541' as code,'car_dealership' as fclass,name,way from planet_osm_point where shop='car' ;
# select osm_id,'2542' as code,'bicycle_shop' as fclass,name,way from planet_osm_point where shop='bicycle' ;
# select osm_id,'2543' as code,'doityourself' as fclass,name,way from planet_osm_point where shop='doityourself' or shop='hardware' ;
# select osm_id,'2544' as code,'furniture_shop' as fclass,name,way from planet_osm_point where shop='furniture' ;
# select osm_id,'2546' as code,'computer_shop' as fclass,name,way from planet_osm_point where shop='computer' ;
# select osm_id,'2547' as code,shop as fclass,name,way from planet_osm_point where shop='garden_centre' ;
# select osm_id,'2561' as code,shop as fclass,name,way from planet_osm_point where shop='hairdresser' ;
# select osm_id,'2562' as code,shop as fclass,name,way from planet_osm_point where shop='car_repair' ;
# select osm_id,'2563' as code,amenity as fclass,name,way from planet_osm_point where amenity='car_rental' ;
# select osm_id,'2564' as code,amenity as fclass,name,way from planet_osm_point where amenity='car_wash' ;
# select osm_id,'2565' as code,amenity as fclass,name,way from planet_osm_point where amenity='car_sharing' ;
# select osm_id,'2566' as code,amenity as fclass,name,way from planet_osm_point where amenity='bicycle_rental' ;
# select osm_id,'2567' as code,'travel_agent' as fclass,name,way from planet_osm_point where shop='travel_agency' ;
# select osm_id,'2568' as code,'laundry' as fclass,name,way from planet_osm_point where shop='laundry' or shop='dry_cleaning' ;
## select osm_id,'2590' as code,amenity as fclass,name,way from planet_osm_point where amenity='vending_machine' and vending!='cigarettes' and vending!='parking_tickets';
# select osm_id,'2590' as code,amenity as fclass,name,way from planet_osm_point where amenity='vending_machine' ; ### FIX
## select osm_id,'2591' as code,'vending_cigarette' as fclass,name,way from planet_osm_point where amenity='vending_machine' and vending='cigarettes' ;
## select osm_id,'2592' as code,'vending_parking' as fclass,name,way from planet_osm_point where amenity='vending_machine' and vending='parking_tickets' ;
# select osm_id,'2601' as code,amenity as fclass,name,way from planet_osm_point where amenity='bank' ;
# select osm_id,'2602' as code,amenity as fclass,name,way from planet_osm_point where amenity='atm' ;
# select osm_id,'2701' as code,'tourist_info' as fclass,name,way from planet_osm_point where tourism='information';
## select osm_id,'2701' as code,'tourist_info' as fclass,name,way from planet_osm_point where tourism='information' and infromation!='map' and infromation!='board' and infromation!='guidepost'  ;
## select osm_id,'2704' as code,'tourist_map' as fclass,name,way from planet_osm_point where tourism='information' and infromation='map' ;
## select osm_id,'2705' as code,'tourist_board' as fclass,name,way from planet_osm_point where tourism='information' and infromation='board' ;
## select osm_id,'2706' as code,'tourist_guidepost' as fclass,name,way from planet_osm_point where tourism='information' and infromation='guidepost' ;
# select osm_id,'2721' as code,tourism as fclass,name,way from planet_osm_point where tourism='attraction' ;
# select osm_id,'2722' as code,tourism as fclass,name,way from planet_osm_point where tourism='museum' ;
# select osm_id,'2723' as code,historic as fclass,name,way from planet_osm_point where historic='monument' ;
# select osm_id,'2724' as code,historic as fclass,name,way from planet_osm_point where historic='memorial' ;
# select osm_id,'2725' as code,'art' as fclass,name,way from planet_osm_point where historic='artwork' ;
# select osm_id,'2731' as code,historic as fclass,name,way from planet_osm_point where historic='castle' ;
# select osm_id,'2732' as code,historic as fclass,name,way from planet_osm_point where historic='ruins' ;
# select osm_id,'2733' as code,'archaeological' as fclass,name,way from planet_osm_point where historic='archaeological_site' ;
# select osm_id,'2734' as code,'wayside_cross' as fclass,name,way from planet_osm_point where historic='wayside_criss' ;
# select osm_id,'2735' as code,historic as fclass,name,way from planet_osm_point where historic='wayside_shrine' ;
# select osm_id,'2736' as code,historic as fclass,name,way from planet_osm_point where historic='battlefield' ;
# select osm_id,'2737' as code,historic as fclass,name,way from planet_osm_point where historic='fort' ;
# select osm_id,'2741' as code,historic as fclass,name,way from planet_osm_point where historic='picnic_site' ;
# select osm_id,'2742' as code,historic as fclass,name,way from planet_osm_point where historic='viewpoint' ;
# select osm_id,'2743' as code,historic as fclass,name,way from planet_osm_point where historic='zoo' ;
# select osm_id,'2744' as code,historic as fclass,name,way from planet_osm_point where historic='theme_park' ;
# select osm_id,'2901' as code,amenity as fclass,name,way from planet_osm_point where amenity='toilets' ;
# select osm_id,'2902' as code,amenity as fclass,name,way from planet_osm_point where amenity='bench' ;
# select osm_id,'2903' as code,amenity as fclass,name,way from planet_osm_point where amenity='drinking_water' ;
# select osm_id,'2904' as code,amenity as fclass,name,way from planet_osm_point where amenity='fountain' ;
# select osm_id,'2905' as code,amenity as fclass,name,way from planet_osm_point where amenity='hunting_stand' ;
# select osm_id,'2906' as code,amenity as fclass,name,way from planet_osm_point where amenity='waste_basket' ;
# select osm_id,'2907' as code,'camera_surveillance' as fclass,name,way from planet_osm_point where man_made='surveillance' ;
# select osm_id,'2921' as code,'emergency_phone' as fclass,name,way from planet_osm_point where amenity='emergency_phone' ; ###FIX
## select osm_id,'2921' as code,'emergency_phone' as fclass,name,way from planet_osm_point where amenity='emergency_phone' or emergency='phone' ;
# select osm_id,'2922' as code,amenity as fclass,name,way from planet_osm_point where amenity='fire_hydrant' ; ###FIX
## select osm_id,'2922' as code,amenity as fclass,name,way from planet_osm_point where amenity='fire_hydrant' or emergency='fire_hydrant' ;
# select osm_id,'2923' as code,'emergency_access' as fclass,name,way from planet_osm_point where highway='emergency_access_point' ;
# select osm_id,'2950' as code,man_made as fclass,name,way from planet_osm_point where man_made='tower' and "tower:type"!='communication' and "tower:type"!='observation' ;
# select osm_id,'2951' as code,'tower_comms' as fclass,name,way from planet_osm_point where man_made='tower' and "tower:type"='communication' ;
# select osm_id,'2952' as code,'tower_observation' as fclass,name,way from planet_osm_point where man_made='water_tower' ;
# select osm_id,'2953' as code,man_made as fclass,name,way from planet_osm_point where man_made='tower' and "tower:type"='observation' ;
# select osm_id,'2954' as code,man_made as fclass,name,way from planet_osm_point where man_made='windmill' ;
# select osm_id,'2955' as code,man_made as fclass,name,way from planet_osm_point where man_made='lighthouse' ;
# select osm_id,'2961' as code,man_made as fclass,name,way from planet_osm_point where man_made='wastewater_plant' ;
# select osm_id,'2962' as code,man_made as fclass,name,way from planet_osm_point where man_made='water_wel' ;
# select osm_id,'2963' as code,'water_mill' as fclass,name,way from planet_osm_point where man_made='watermill' ;
# select osm_id,'2964' as code,man_made as fclass,name,way from planet_osm_point where man_made='water_works' ;
class Pois(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

# select osm_id,'3100' as code,religion as fclass,name,way from planet_osm_point where religion='christian' and denomination not in ('anglican','catholic','evangelical','lutheran','methodist','orthodox','protestant','baptist','mormon') ;    
# select osm_id,'3101' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='anglican' ;    
# select osm_id,'3102' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='catholic' ;    
# select osm_id,'3103' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='evangelical' ;    
# select osm_id,'3104' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='lutheran' ;    
# select osm_id,'3105' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='methodist' ;    
# select osm_id,'3106' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='orthodox' ;    
# select osm_id,'3107' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='protestant' ;    
# select osm_id,'3108' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='baptist' ;    
# select osm_id,'3109' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='christian' and denomination='mormon' ;
# select osm_id,'3200' as code,religion as fclass,name,way from planet_osm_point where religion='jewish' ;    
# select osm_id,'3300' as code,religion as fclass,name,way from planet_osm_point where religion='muslim' and denomination not in ('sunni','shia') ;
# select osm_id,'3301' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='muslim' and denomination='sunni';
# select osm_id,'3302' as code,religion||'_'||denomination as fclass,name,way from planet_osm_point where religion='muslim' and denomination='shia';
class Pofw(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

# select osm_id,'4101' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='spring' ;    
# select osm_id,'4103' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='glacier' ;    
# select osm_id,'4111' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='peak' ;    
# select osm_id,'4112' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='cliff' ;    
# select osm_id,'4113' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='volcano' ;    
# select osm_id,'4121' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='tree' ;
# select osm_id,'4131' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='mine' ;
# select osm_id,'4132' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='cave_entrance' ;
# select osm_id,'4141' as code,"natural" as fclass,name,way from planet_osm_point where "natural"='beach' ;
class Natural(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    
    
# select osm_id,'5601' as code,railway as fclass,name,way from planet_osm_point where railway='station' ;
# select osm_id,'5602' as code,'railway_'||railway as fclass,name,way from planet_osm_point where railway='halt' ;
# select osm_id,'5603' as code,railway as fclass,name,way from planet_osm_point where railway='tram_stop' ;
# select osm_id,'5621' as code,highway as fclass,name,way from planet_osm_point where highway='bus_stop' ;
# select osm_id,'5622' as code,amenity as fclass,name,way from planet_osm_point where amenity='bus_station' ;
# select osm_id,'5641' as code,amenity as fclass,name,way from planet_osm_point where amenity='taxi_rank' ;
# select osm_id,'5651' as code,amenity as fclass,name,way from planet_osm_point where amenity='airport' ;
# select osm_id,'5652' as code,amenity as fclass,name,way from planet_osm_point where amenity='airfield' or military='airfield' ;
# select osm_id,'5655' as code,aeroway as fclass,name,way from planet_osm_point where aeroway='helipad' ;
# select osm_id,'5656' as code,aeroway as fclass,name,way from planet_osm_point where aeroway='apron' ;
# select osm_id,'5661' as code,amenity as fclass,name,way from planet_osm_point where amenity='ferry_terminal' ;
# select osm_id,'5671' as code,'aeroway_station' as fclass,name,way from planet_osm_point where aeroway='station' ;
class Transport(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

# select osm_id,'5111' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='motorway' ;
# select osm_id,'5112' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='trunk' ;
# select osm_id,'5113' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='primary' ;
# select osm_id,'5114' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='secondary' ;
# select osm_id,'5115' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='tertiary' ;
# select osm_id,'5121' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='unclassified' ;
# select osm_id,'5122' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='residential' ;
# select osm_id,'5123' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='living_street' ;
# select osm_id,'5124' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='pedestrian' ;
# select osm_id,'5131' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='motorway_link' ;
# select osm_id,'5132' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='trunk_link' ;
# select osm_id,'5133' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='primary_link' ;
# select osm_id,'5134' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='secondary_link' ;
# select osm_id,'5141' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='service' ;
# select osm_id,'5142' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype not in ('grade1','grade2','grade3','grade4','grade5') ;
# select osm_id,'5143' as code,highway||'_'||tracktype as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype='grade1' ;
# select osm_id,'5144' as code,highway||'_'||tracktype as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype='grade2' ;
# select osm_id,'5145' as code,highway||'_'||tracktype as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype='grade3' ;
# select osm_id,'5146' as code,highway||'_'||tracktype as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype='grade4' ;
# select osm_id,'5147' as code,highway||'_'||tracktype as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='track' and tracktype='grade5' ;
# select osm_id,'5151' as code,'bridleway' as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='bridleway' or (highway='path' and horse='designated') ;
# select osm_id,'5152' as code,'cycleway' as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='cycleway' or (highway='path' and cycle='designated') ;
## select osm_id,'5153' as code,'footway' as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='footway' or (highway='path' and foot='designated') ;
## select osm_id,'5154' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='path' and horse!='designated' and cycle!='designated' and foot!='designated' ;
# select osm_id,'5155' as code,highway as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='steps' ;
# select osm_id,'5199' as code,'unknown' as fclass,name,ref,oneway,layer,bridge,tunnel,way from planet_osm_roads where highway='road' ;
class Roads(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    ref = models.CharField(max_length=20)
    oneway = models.CharField(max_length=1)
    maxspeed = models.IntegerField()
    layer = models.FloatField()
    bridge = models.CharField(max_length=1)
    tunnel = models.CharField(max_length=1)
    geom_multilinestring = models.MultiLineStringField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

# select osm_id,'5201' as code,highway as fclass,name,way from planet_osm_point where highway='traffic_signals' ;
# select osm_id,'5202' as code,highway as fclass,name,way from planet_osm_point where highway='mini_roundabout' ;
# select osm_id,'5203' as code,highway as fclass,name,way from planet_osm_point where highway='stop' ;
# select osm_id,'5204' as code,'crossing' as fclass,name,way from planet_osm_point where highway='crossing' or railway='level_crossing' ;
# select osm_id,'5205' as code,highway as fclass,name,way from planet_osm_point where highway='speed_camera' ;
# select osm_id,'5206' as code,highway as fclass,name,way from planet_osm_point where highway='motorway_junction' ;
# select osm_id,'5207' as code,highway as fclass,name,way from planet_osm_point where highway='turning_circle' ;
# select osm_id,'5208' as code,highway as fclass,name,way from planet_osm_point where highway='ford' ;
# select osm_id,'5209' as code,highway as fclass,name,way from planet_osm_point where highway='street_lamp' ;
# select osm_id,'5250' as code,amenity as fclass,name,way from planet_osm_point where amenity='fuel' ;
# select osm_id,'5251' as code,'service' as fclass,name,way from planet_osm_point where highway='services' ;
# select osm_id,'5260' as code,amenity as fclass,name,way from planet_osm_point where amenity='parking' ; ###FIX
## select osm_id,'5260' as code,amenity as fclass,name,way from planet_osm_point where amenity='parking' and parking not in ('site','multi-storey','underground') ;
## select osm_id,'5261' as code,'parking_site' as fclass,name,way from planet_osm_point where amenity='parking' and parking='site' ;
## select osm_id,'5262' as code,'parking_multistorey' as fclass,name,way from planet_osm_point where amenity='parking' and parking='multi-storey' ;
## select osm_id,'5263' as code,'parking_underground' as fclass,name,way from planet_osm_point where amenity='parking' and parking='underground' ;
# select osm_id,'5270' as code,'parking_bicycle' as fclass,name,way from planet_osm_point where amenity='bicycle_parking' ;
# select osm_id,'5301' as code,leisure as fclass,name,way from planet_osm_point where leisure='slipway' ;
# select osm_id,'5302' as code,leisure as fclass,name,way from planet_osm_point where leisure='marina' ;
# select osm_id,'5303' as code,man_made as fclass,name,way from planet_osm_point where man_made='pier' ;
# select osm_id,'5311' as code,waterway as fclass,name,way from planet_osm_point where waterway='dam' ;
# select osm_id,'5321' as code,waterway as fclass,name,way from planet_osm_point where waterway='waterfall' ;
# select osm_id,'5331' as code,waterway as fclass,name,way from planet_osm_point where waterway='lock_gate' ;
# select osm_id,'5332' as code,waterway as fclass,name,way from planet_osm_point where waterway='weir' ;
class Traffic(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipoint = models.MultiPointField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

# select osm_id,'6101' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='rail' ;
# select osm_id,'6102' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='light_rail' ;
# select osm_id,'6103' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='subway' ;
# select osm_id,'6104' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='tram' ;
# select osm_id,'6105' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='monorail' ;
# select osm_id,'6106' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='narrow_gauge' ;
# select osm_id,'6107' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='miniature' ;
# select osm_id,'6108' as code,railway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='funicular' ;
# select osm_id,'6109' as code,rack as fclass,name,layer,bridge,tunnel,way from planet_osm_line where railway='rack' ;
# select osm_id,'6111' as code,aerialway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway='drag_lift' ;
# select osm_id,'6112' as code,aerialway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway='chair_lift' ;
# select osm_id,'6113' as code,aerialway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway='cable_car' ;
# select osm_id,'6114' as code,aerialway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway='gondola' ;
# select osm_id,'6115' as code,aerialway as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway='goods' ;
# select osm_id,'6119' as code,'other_lift' as fclass,name,layer,bridge,tunnel,way from planet_osm_line where aerialway in ('platter','t-bar','j-bar','magic_carpet','zip_line','rope_tow','mixed_lift') ;
class Railways(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    layer = models.FloatField()
    bridge = models.CharField(max_length=1)
    tunnel = models.CharField(max_length=1)
    geom_multilinestring = models.MultiLineStringField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

class Landuse(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipolygon = models.MultiPolygonField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

class Waterways(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    width = models.IntegerField()
    name = models.CharField(max_length=100)
    geom_multilinestring = models.MultiLineStringField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    

class Water(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    country = models.ForeignKey(Country)
    osm_id = models.CharField(max_length=10)
    code = models.IntegerField()
    fclass = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    geom_multipolygon = models.MultiPolygonField(srid=4326,blank=True, null=True)

    objects = models.GeoManager()

    def __str__(self):
        return str(self.id)    
    


'''
#################################################
#10xx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_places" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"population" numeric(10,0),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_places" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_places','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_places";

#15xx
Shapefile type: Polygon
Postgis type: MULTIPOLYGON[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_buildinqs" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100),
"type" varchar(20));
ALTER TABLE "public"."hikerdb_buildinqs" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_buildinqs','geom','4326','MULTIPOLYGON',2);
COMMIT;
ANALYZE "public"."hikerdb_buildinqs";

#2xxx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_pois" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_pois" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_pois','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_pois";

#3xxx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_pofw" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_pofw" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_pofw','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_pofw";

#41xx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_natural" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_natural" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_natural','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_natural";

#50xx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_transport" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_transport" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_transport','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_transport";

#51xx
Shapefile type: Arc
Postgis type: MULTILINESTRING[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_roads" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100),
"ref" varchar(20),
"oneway" varchar(1),
"maxspeed" int2,
"layer" float8,
"bridge" varchar(1),
"tunnel" varchar(1));
ALTER TABLE "public"."hikerdb_roads" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_roads','geom','4326','MULTILINESTRING',2);
COMMIT;
ANALYZE "public"."hikerdb_roads";

#52xx
Shapefile type: Point
Postgis type: POINT[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_traffic" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_traffic" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_traffic','geom','4326','POINT',2);
COMMIT;
ANALYZE "public"."hikerdb_traffic";

#61xx
Shapefile type: Arc
Postgis type: MULTILINESTRING[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_railways" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_railways" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_railways','geom','4326','MULTILINESTRING',2);
COMMIT;
ANALYZE "public"."hikerdb_railways";

#72xx
Shapefile type: Polygon
Postgis type: MULTIPOLYGON[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_landuse" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_landuse" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_landuse','geom','4326','MULTIPOLYGON',2);
COMMIT;
ANALYZE "public"."hikerdb_landuse";

#81xx
Shapefile type: Arc
Postgis type: MULTILINESTRING[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_waterways" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"width" int4,
"name" varchar(100));
ALTER TABLE "public"."hikerdb_waterways" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_waterways','geom','4326','MULTILINESTRING',2);
COMMIT;
ANALYZE "public"."hikerdb_waterways";

#82xx
Shapefile type: Polygon
Postgis type: MULTIPOLYGON[2]
SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "public"."hikerdb_water" (gid serial,
"osm_id" varchar(10),
"code" int2,
"fclass" varchar(20),
"name" varchar(100));
ALTER TABLE "public"."hikerdb_water" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('public','hikerdb_water','geom','4326','MULTIPOLYGON',2);
COMMIT;
ANALYZE "public"."hikerdb_water";
'''