Feature: Custom rectangle drawer -
  Draw a rectangle using given attributes

  @rectangle
  Scenario: Rectangle 3x3 using *
    Given we have a rectangle drawer
    And we want to use *
    And we want our length to be 3
    And we want our width to be 3
    When we want to draw a rectangle using given attributes
    Then the result is a rectangle 3x3 using * sign


  @rectangle
  Scenario: Rectangle 3x4 using V
    Given we have a rectangle drawer
    And we want to use V
    And we want our length to be 3
    And we want our width to be 4
    When we want to draw a rectangle using given attributes
    Then the result is a rectangle 3x4 using V sign


  @rectangle
  Scenario: Rectangle 10x5 using |
    Given we have a rectangle drawer
    And we want to use |
    And we want our length to be 10
    And we want our width to be 5
    When we want to draw a rectangle using given attributes
    Then the result is a rectangle 10x5 using | sign

  @rectangle
  Scenario: Rectangle 1x5 using s
    Given we have a rectangle drawer
    And we want to use s
    And we want our length to be 1
    And we want our width to be 5
    When we want to draw a rectangle using given attributes
    Then the result is a horizontal line with a length 5 using s sign


  @rectangle
  Scenario: Rectangle 5x1 using x
    Given we have a rectangle drawer
    And we want to use x
    And we want our length to be 5
    And we want our width to be 1
    When we want to draw a rectangle using given attributes
    Then the result is a vertical line with a length 5 using x sign


  @rectangle
  Scenario: Rectangle 0x3 using *
    Given we have a rectangle drawer
    And we want to use *
    And we want our length to be 0
    And we want our width to be 3
    When we want to draw a rectangle using given attributes
    Then the program should return wrong input error


  @rectangle
  Scenario: Rectangle 3x0 using *
    Given we have a rectangle drawer
    And we want to use *
    And we want our length to be 3
    And we want our width to be 0
    When we want to draw a rectangle using given attributes
    Then the program should return wrong input error


  @rectangle
  Scenario: Rectangle 0x0 using *
    Given we have a rectangle drawer
    And we want to use *
    And we want our length to be 0
    And we want our width to be 0
    When we want to draw a rectangle using given attributes
    Then the program should return wrong input error