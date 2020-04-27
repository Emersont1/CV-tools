# CV-tools
Set of tools to make CVs from a JSON

## Example JSON
```JSON
{
  "name": "Harry Potter",
  "email": "harry@privetdrive.uk",
  "desc": "I'm a wizard (called Harry)",
  "sections": [
    {
      "name": "Education and Qualifications",
      "sections": [
        {
          "name": "NEWTs, Studied",
          "when": "skipped due to second Wizarding War",
          "where": "Hogwarts School Of WitchCraft And Wizardry",
          "type": "results_htable",
          "cols": 2,
          "data": {
            "Care of Magical Creatures": "Exempted",
            "Charms": "Exempted",
            "Defence Against the Dark Arts": "Exempted",
            "Herbology": "Exempted",
            "Potions": "Exempted",
            "Transfiguration": "Exempted"
          }
        },
        {
          "name": "OWLs",
          "when": "Taken June 1996",
          "where": "Hogwarts School Of WitchCraft And Wizardry",
          "type": "results_vtable",
          "cols": 2,
          "data": [
            "Astronomy A",
            "Care of Magical Creatures E",
            "Charms E",
            "Defense Against the\nDark Arts O",
            "Divination P",
            "Herbology E",
            "History of Magic D",
            "Potions E",
            "Transfiguration E"
          ]
        }
      ]
    },
    {
      "type": "column_break"
    },
    {
      "name": "Skills",
      "type": "list",
      "data": [
        {
          "head": "Horcrux Destruction",
          "data": "Tom Riddle's Diary, 1991"
        },
        {
          "head": "Duelling"
        }
      ],
      "sections": [
        {
          "name": "News Appearances",
          "type": "list",
          "data": [
            {
              "data": "An interview with the quibbler",
              "url": "https://quibbler.org/1996/february/interview-harry-potter"
            },
            {
              "data": "The Chosen One: Article in the daily Prophet",
              "url": "https://quibbler.org/1996/february/interview-harry-potter"
            },
            {
              "data": "Undesirable No1: Anti Me Propaganda (2nd Wizarding War)",
              "url": "https://archive.magic.gov/Undesirable"
            }
          ]
        },
        {
          "name": "Other Skills",
          "type": "text",
          "data": "Horcrux desturction, and general stopping of dark and evil wizards"
        }
      ]
    },
    {
      "type": "h_rule"
    },
    {
      "name": "Past Employment",
      "type": "employment",
      "data": [
        {
          "when": "2007-2016",
          "name": "Auror Office, Ministry of Magic",
          "where": "London",
          "more": "During this time, I revolutionised the Auror Department."
        },
        {
          "when": "2017-",
          "name": "Head of the Department of Magical Law Enforcement , Ministry of Magic",
          "where": "London",
          "more": "Hermione had fudge or something (christ that play was bad)"
        }
      ]
    }
  ]
}
```
