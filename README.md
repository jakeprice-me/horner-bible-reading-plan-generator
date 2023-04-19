# Horner Bible Reading Plan Generator

This script generates a list of readings for the Horner Bible Reading Plan. You can read more about this reading plan [here](./horner_bible_reading_plan.pdf). 

The plan recommends using physical bookmarks in your bible, and moving each bookmark through each list as you progress. Personally I don't bother with the bookmarks and instead prefer a list I can work through and check off. If you've ever come across this plan before however (perhaps in a bible app), you'll find that once you go past the first year, you'll struggle to find any resources for the second year and onwards. So, this script aims to fix that and provide readers with lists for as long as they plan to do it.

## Configuration

The configuration file `config.yml` is crucial to the script working. 

`readings_start` and `readings_end` specify the days you want to generate readings for. The script is "clever" enough to generate the correct readings for any day, spitting out readings as if you'd read through each list up until the day specified. So, if you specify a `readings_start` date of 654 the list will output the readings that you would be on if you'd worked through each list for the past 653 days.

### Readings Start & End Examples

The below values would generate the first year of readings.

```yaml
readings_start: 0
readings_end: 365
```

Whereas this example would generate the second year of readings.

```yaml
readings_start: 366
readings_end: 731
```

The script runs very quickly, so you can easily generate 10 years or more of readings in no time.

### Reading Lists

The reading lists are specified under `list_1`, `list_2`, `list_3` and so on up to `list_10`. You can adjust these if need be (some people swap Acts with another book for example, but you need to make sure that the format stays the same as the below.

```yaml
list_n:
    - Book, Number of Chapters
```

## Usage

Run the script as you would any other Python script.

```shell
python main.py
```

## Output

You'll get a list of readings, which you can either take as is, or massage into another format (markdown checkbox list for example).

```
366, Matthew 10, Deuteronomy 26, Ephesians 3, 2 John 1, Song of Solomon 2, Psalms 66, Proverbs 25, 1 Kings 13, Jeremiah 50, Acts 2
367, Matthew 11, Deuteronomy 27, Ephesians 4, 3 John 1, Song of Solomon 3, Psalms 67, Proverbs 26, 1 Kings 14, Jeremiah 51, Acts 3
368, Matthew 12, Deuteronomy 28, Ephesians 5, Jude 1, Song of Solomon 4, Psalms 68, Proverbs 27, 1 Kings 15, Jeremiah 52, Acts 4
369, Matthew 13, Deuteronomy 29, Ephesians 6, Revelation 1, Song of Solomon 5, Psalms 69, Proverbs 28, 1 Kings 16, Lamentations 1, Acts 5
370, Matthew 14, Deuteronomy 30, Philippians 1, Revelation 2, Song of Solomon 6, Psalms 70, Proverbs 29, 1 Kings 17, Lamentations 2, Acts 6
371, Matthew 15, Deuteronomy 31, Philippians 2, Revelation 3, Song of Solomon 7, Psalms 71, Proverbs 30, 1 Kings 18, Lamentations 3, Acts 7
372, Matthew 16, Deuteronomy 32, Philippians 3, Revelation 4, Song of Solomon 8, Psalms 72, Proverbs 31, 1 Kings 19, Lamentations 4, Acts 8
373, Matthew 17, Deuteronomy 33, Philippians 4, Revelation 5, Job 1, Psalms 73, Proverbs 1, 1 Kings 20, Lamentations 5, Acts 9
374, Matthew 18, Deuteronomy 34, Colossians 1, Revelation 6, Job 2, Psalms 74, Proverbs 2, 1 Kings 21, Ezekiel 1, Acts 10
375, Matthew 19, Genesis 1, Colossians 2, Revelation 7, Job 3, Psalms 75, Proverbs 3, 1 Kings 22, Ezekiel 2, Acts 11
376, Matthew 20, Genesis 2, Colossians 3, Revelation 8, Job 4, Psalms 76, Proverbs 4, 2 Kings 1, Ezekiel 3, Acts 12
```

## Future Improvements

I plan on adding a few styles of output in the future (plain text, csv, markdown etc), and a few different output formats (html, text, pdf, etc).

