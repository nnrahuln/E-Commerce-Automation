Feature: Login

  Scenario Outline: Login with different users
    Given I open the SauceDemo website
    When I login with username "<username>" and password "<password>"
    Then I should see the login result "<result>"

    Examples:
      | username        | password     | result  |
      | standard_user   | secret_sauce | success |
      | locked_out_user | secret_sauce | locked  |