# Authentication-practice

working with request

randommer link: https://randommer.io/

## create virtual environment
```bash
python -m venv venv
```

## activate
windows
```bash
source venv/Scripts/activate
```
linux | mac
```bash
source venv/bin/activate
```

## pip install
```bash
pip install -r requirements.txt
```

## Randommer

properties:
- base_url

methods:
- get_url()


## Card
### create Card class

properties:
- base_url

methods:
- get_card()
- get_card_types()
- get_url()

## Finance
### cleate Finance class

properties:
- base_url

methods:
- get_url()
- get_crypto_address_types()
- get_crypto_address()
- get_countries()
- get_iban_by_country_code()

## Misc
### cleate Misc class

properties:
- base_url

methods:
- get_url()
- get_cultures()
- get_random_address()

## Name
### cleate Name class

properties:
- base_url

methods:
- get_url()
- get_name()
- get_name_suggestions()
- get_name_cultures()

## Phone
### cleate Phone class

properties:
- base_url

methods:
- get_url()
- generate()
- get_IMEI()
- is_valid()
- get_countries()

## SocialNumber
### cleate SocialNumber class

properties:
- base_url

methods:
- get_url()
- get_SocialNumber()

## Text
### cleate Text class

properties:
- base_url

methods:
- get_url()
- generate_LoremIpsum()
- generate_password()

