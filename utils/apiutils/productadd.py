class AddProductCart:

    def producttocart(self, api_context, products):

        for product in products:
            product_id = product['id']
            qty = str(product.get("quantity",1))
            payload = {}

            if product.get("type") == 'giftcard':
               payload[f'addtocart_{product_id}.EnteredQuantity'] = qty

               for field, value in product["attributes"].items():
                   payload[f'giftcard_{product_id}.{field}'] = value

               response = api_context.post(f'addproducttocart/details/{product_id}/1', form = payload)

            elif product.get("type") == "attribute":
               payload[f'addtocart_{product_id}.EnteredQuantity'] = qty

               for k,v in product["attributes"].items():
                  payload[k] = v
               response = api_context.post(f"addproducttocart/details/{product_id}/1", form = payload)
            else:
               response = api_context.post(f"addproducttocart/catalog/{product_id}/1/{qty}")

            assert response.ok, f'Failed to add product {product_id}'



