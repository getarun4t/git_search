Feature: Creating a Gist
Ability to create a gist in the github website

    Scenario: To test the ability of the user to login and create a gist 
        Given User is opening login page
        And User is logging in
        When User clicks on + in the top panel and selects New Gist
        And User is entering the description and filename
        And User is clicking on Create Public gist button
        Then User has created a public gist

	Scenario: To test the ability of the user to login and create a private gist 
        Given User is opening login page
        And User is logging in
        When User clicks on + in the top panel and selects New Gist
        And User is entering the description and filename
        And User is clicking on Create private gist button
        Then User has created a private gist
        And User is logging out