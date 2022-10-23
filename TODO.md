## Action Items

There's a few things you need to do in supabase before we can link this application to it. From my understanding of supabase, you create "projects" to do this stuff. So if you mess up we can just delete the bad project.

> The default options for a free project are more than good enough. 

### Database Work

In supabase make 3 tables for your data:

A `users` table with these columns:
- username (char 25)
- password (char 25)

A `species` table with these columns:
- plant_id (char 256)
- scientific_name (char 256)
- common_name (char 256)
- image_url (char 128)
- description (text)

A `survey_data` table: 
- plant_id (char 256)
- flowering_stage (char 50)
- location (char 25)
- number_of_inflorescences (int?)
- number_of_flowers (int?)
- fruiting_stage (char 50)
- number_of_fruits (int?)
- comments (char 256)

<br> 

> Optional tables that might help us later.

A `species_locations` table to track where each plant should be: 
- plant_id (char 256)
- location_id (char 25)

A `locations` table with these columns:
- location_id (char 25)
- map_url (char 128)

<br>

### API Key

> This is needed to link supabase to our replit. 

Lastly generate a API key in supabase and save it in the secrets (the padlock icon) section here. I'm not sure where in supabase you do this, click around the project to figure it out. 
