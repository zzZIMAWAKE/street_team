# Initial code review

* Storage of rewards data should probably use a database, a database will allow us to persist data between services
  being shut down or crashing and would also enable us to deal with more complex structures such as several campaigns
  being run at once. Understandably there is a comment addressing this but it would still be mentioned in a review.
* Class name(object) < object no longer required. This is done implicitly in python 3
* queueService - variable names should be snake case - queue_service
* 'sales' queue is currently hardcoded in the start_consuming method in the queue service,
  instead this should be part of the initialisation to allow reuse between different services
* We should store credentials and queue / exchange names in a config file
* Points from purchase function currently takes a 'price' variable, to stay consistent with the sales data we receive
  which provides 'cost' we should rename this function to be points_from_cost with a variable named cost.
* RewardsEngine is slightly confusing as it stands, I feel a SalesEngine might be a better approach,
  ingesting all the sales data from the queue, storing it that way we can easily return recommended rewards
  on demand based on the points data in the database - at the moment the current system returns reward
  recommendations upon each sale which seems overkill and unnecessary it is much more likely that a user will
  make several sales and then request reward recommendations based on their current points.
  As it stands now I left it as RewardsEngine as the requested implementation adds reward recommendations
  to the queue via the RewardsEngine which makes the name meaningful, although I feel its implementation is
  being misused currently.
* Current structure seems a little hard to follow, services appear in several places & the package names seem too
  specific for this project to grow nicely, I'd prefer to see services & engines packages but I respect that
  with the current implementation imports can become a problem with services being run directly from the command line.
  This could be solved with a main.py or something similar in the src package that would control the flow of services
  being launched.
* It is unclear what categories currently stand for within the rewards data, some explanation of this would be required.
