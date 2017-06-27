# Future improvements

* I created a database for easy storage of the data and to keep data persistent, the next steps in this project
  will ultimately require persistent storage, so I thought it was beneficial
  to implement as it seems highly likely to be required in the future. Here are a few examples of where I feel
  persistent data storage will be required in the future of this project:

   * to keep track of points
   * to enable users to spend their points
   * to keep track of global uses
   * to keep track of users claimed rewards

* Currently global max uses is not considered as no one is actually purchasing any rewards,
  just being given recommendations, future improvements will probably include purchases,
  and it will need to adapt to this by adding checks for global max uses, whether that happens
  in the current reward table (or should those numbers be needed for reference) a new table that
  tracks the rewards usages

* Adding a config file for credentials would be a good idea

* Some kind of restructure as mentioned in the initial review would be a good idea should this project be expected to
grow substantially over time

