Feature: Common Steps
Used to store the common steps which are used across test cases

Scenario: Opening and logging into the git dashboard
	Given User is opening login page
	And User is logging in
	
Scenario: Opening Gists Search
	Given User is opening the gist page	
	
Scenario: Opening Gists Search and logging in
	Given User is opening the gist page	
	And User is logging into Gist