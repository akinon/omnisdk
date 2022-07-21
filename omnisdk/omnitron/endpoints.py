from omnisdk.api_endpoint import ApiEndpoint
from omnisdk.omnitron.models import *


class OmnitronApiEndpoint(ApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(api_class_name="OmnitronApiClient", *args, **kwargs)


class ProductEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="products", model=Product, *args, **kwargs)


class CatalogEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="catalogs", model=Catalog, *args, **kwargs)


class ChannelEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channels", model=Channel, *args, **kwargs)


class OrderByNumberEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="order_number", model=Order, *args, **kwargs)


class OrderItemEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="order_items", model=OrderItem,
                         *args, **kwargs)


class PaymentOptionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="payment_options", model=PaymentOption,
                         *args, **kwargs)


class TransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="transactions",
                         model=Transaction, *args, **kwargs)


class OrderTransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="order_transactions",
                         model=OrderTransaction, *args, **kwargs)


class PayOnDeliveryTransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="pay_on_delivery_transactions",
                         model=PayOnDeliveryTransaction, *args, **kwargs)


class LoyaltyTransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="loyalty_transactions",
                         model=LoyaltyTransaction, *args, **kwargs)


class FundsTransferTransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="funds_transfer_transactions",
                         model=FundsTransferTransaction, *args, **kwargs)


class BexTransactionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="bex_transactions",
                         model=BexTransaction, *args, **kwargs)


class ChannelCategoryTreeEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/category_trees",
                         model=CategoryTree, *args, **kwargs)


class ChannelCategoryNodeEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/category_nodes",
                         model=CategoryNode, *args, **kwargs)


class ChannelCancellationReasonEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/cancellation_reasons",
                         model=CancellationReason, *args, **kwargs)


class ChannelCancellationRequestEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/cancellation_requests",
                         model=CancellationRequest, *args, **kwargs)


class ChannelAttributeSetConfigEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_set_configs",
                         model=ChannelAttributeSetConfig, *args, **kwargs)


class ChannelAttributeSetEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_sets",
                         model=ChannelAttributeSet, *args, **kwargs)


class ChannelAttributeEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attributes",
                         model=ChannelAttribute, *args, **kwargs)


class ChannelAttributeSchemaEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_schemas",
                         model=ChannelAttributeSchema, *args, **kwargs)


class ChannelAttributeConfigEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_configs",
                         model=ChannelAttributeConfig, *args, **kwargs)


class ChannelAttributeValueEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_values",
                         model=ChannelAttributeValue, *args, **kwargs)


class ChannelAttributeValueConfigEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/attribute_value_configs",
                         model=ChannelAttributeValueConfig, *args, **kwargs)


class CatalogItemEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="catalog_items",
                         model=CatalogItem, *args, **kwargs)


class ChannelBatchRequestEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/batch_requests",
                         model=BatchRequest, *args, **kwargs)


class ChannelProductEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/products",
                         model=Product, *args, **kwargs)


class ContentTypeEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="content_types",
                         model=ContentType, *args, **kwargs)


class ChannelIntegrationActionEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/integration_actions",
                         model=IntegrationAction, *args, **kwargs)


class ChannelProductPriceEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/product_prices",
                         model=ProductPrice, *args, **kwargs)


class ChannelProductStockEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/product_stocks",
                         model=ProductStock, *args, **kwargs)


class ChannelMappedProductEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/mapped_products",
                         model=Product, *args, **kwargs)


class ChannelProductImageEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/product_images",
                         model=ProductImage, *args, **kwargs)


class ChannelOrderEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/orders",
                         model=Order, *args, **kwargs)


class ChannelCreateOrderEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/create_orders",
                         model=Order, *args, **kwargs)


class ChannelPriceListEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/price_lists",
                         model=PriceList, *args, **kwargs)


class ChannelStockListEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/stock_lists",
                         model=StockList, *args, **kwargs)


class ChannelCargoEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/cargos",
                         model=CargoCompany, *args, **kwargs)


class ChannelCustomerEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/customers",
                         model=Customer, *args, **kwargs)


class ChannelCountryEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/countries",
                         model=Country, *args, **kwargs)


class ChannelCityEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/cities",
                         model=City, *args, **kwargs)


class ChannelTownshipEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/townships",
                         model=Township, *args, **kwargs)


class ChannelDistrictEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/districts",
                         model=District, *args, **kwargs)


class ChannelAddressEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/addresses",
                         model=Address, *args, **kwargs)


class ChannelOrderShippingInfoEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/order_shipping_infos",
                         model=Address, *args, **kwargs)


class ChannelErrorReportEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/error_reports",
                         model=ErrorReport, *args, **kwargs)


class ChannelOrderItemEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/order_items",
                         model=OrderItem, *args, **kwargs)


class ChannelProductCategoryEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/product_categories",
                         model=ProductCategory, *args, **kwargs)


class ChannelExtraProductPriceEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/extra_product_prices",
                         model=ProductPrice, *args, **kwargs)


class ChannelExtraProductStockEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/extra_product_stocks",
                         model=ProductStock, *args, **kwargs)


class ChannelRetailStoreEndpoint(OmnitronApiEndpoint):
    def __init__(self, *args, **kwargs):
        super().__init__(endpoint="channel/{channel_id}/retail_stores",
                         model=RetailStore, *args, **kwargs)
