from dataikuapi import DSSClient
from dataikuapi.dss.recipe import DSSRecipeSettings


host = "http://192.168.0.71:10000"
api_key = "Bp0x6EwIQOmyXMq3PMbco86UEljv99Mr"

client = DSSClient(host, api_key)

project = client.get_project("TEST")

recipes = project.list_recipes("objects")

recipe: DSSRecipeSettings = project.get_recipe("compute_test_dateseT_out").get_definition_and_payload().recipe
recipe.get_settings().get_json_payload()