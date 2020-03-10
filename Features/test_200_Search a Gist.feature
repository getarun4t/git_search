Feature: Searching a Gist
Ability to search a gist in the github website

    Scenario: To test the ability of an unauthenticated user to search a gist 
        Given User is opening the gist page
        When User is searching with the gist name keywords
        Then Public gists are displayed
        And Private gists are not displayed

	Scenario: To test the ability of an authenticated user to search a gist 
        Given User is opening the gist page
        And User is logging into Gist
        When User is searching with the gist name keywords
        Then Public gists are displayed
        And Private gists are displayed