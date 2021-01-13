Feature: Rectangle drawer -
  Draws a rectangle with the given properties using '*'

  Scenario: Two positive different numbers
    Given there is a rectangle drawer
    When we draw a rectangle using length = 3 width = 4
    Then the result is a rectangle 3x4


  Scenario: One positive one negative number
    Given there is a rectangle drawer
    When we draw a rectangle using length = 3 width = -3
    Then the result is Wrong input


  Scenario:  Two positive same numbers
    Given there is a rectangle drawer
    When we draw a rectangle using length = 3 width = 3
    Then the result is a rectangle 3x3


  Scenario: Two negative numbers
    Given there is a rectangle drawer
    When we draw a rectangle using length = -5 width = -2
    Then the result is Wrong input


  Scenario: Two strings instead of integers
    Given there is a rectangle drawer
    When we draw a rectangle using length = 0 width = 0
    Then  the result is Wrong input