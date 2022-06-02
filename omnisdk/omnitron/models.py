import inspect


class BaseModel:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_parameters(self):
        members = inspect.getmembers(self, lambda x: not (inspect.isroutine(x)))
        return {param[0]: param[1] for param in members if not (param[0].startswith('_'))}

    def __str__(self):
        return str(self.get_parameters())


class Address(BaseModel):
    pass


class Country(BaseModel):
    pass


class City(BaseModel):
    pass


class Township(BaseModel):
    pass


class District(BaseModel):
    pass


class RetailStoreGroup(BaseModel):
    pass


class RetailStore(BaseModel):
    pass


class RelatedRetailStore(BaseModel):
    pass


class RetailStoreType(BaseModel):
    pass


class ShippingCost(BaseModel):
    pass


class Application(BaseModel):
    pass


class ApplicationGroup(BaseModel):
    pass


class ApplicationPermission(BaseModel):
    pass


class ApplicationGroupPermission(BaseModel):
    pass


class PriceList(BaseModel):
    pass


class ProductPrice(BaseModel):
    pass


class StockList(BaseModel):
    pass


class ProductStock(BaseModel):
    pass


class PriorityList(BaseModel):
    pass


class ProductPriority(BaseModel):
    pass


class CatalogItem(BaseModel):
    pass


class Catalog(BaseModel):
    pass


class CategoryNode(BaseModel):
    pass


class ProductCategory(BaseModel):
    pass


class CategoryTree(BaseModel):
    pass


class SchemaType(BaseModel):
    pass


class CategoryMappingGroup(BaseModel):
    pass


class CategoryMapping(BaseModel):
    pass


class Channel(BaseModel):
    pass


class CatalogFeedConf(BaseModel):
    pass


class IntegrationAction(BaseModel):
    pass


class IntegrationMapping(BaseModel):
    pass


class ChannelAttributeSet(BaseModel):
    pass


class ChannelAttributeSetConfig(BaseModel):
    pass


class ChannelAttributeSchema(BaseModel):
    pass


class ChannelAttribute(BaseModel):
    pass


class ChannelAttributeConfig(BaseModel):
    pass


class ChannelAttributeValue(BaseModel):
    pass


class ChannelAttributeValueConfig(BaseModel):
    pass


class DataSource(BaseModel):
    pass


class Customer(BaseModel):
    pass


class PanelTranslation(BaseModel):
    pass


class ErrorReport(BaseModel):
    pass


class LoyaltyTransaction(BaseModel):
    pass


class Mapping(BaseModel):
    pass


class Order(BaseModel):
    pass


class OrderItem(BaseModel):
    pass


class Promotion(BaseModel):
    pass


class DiscountItem(BaseModel):
    pass


class BenefitApplicant(BaseModel):
    pass


class ConditionApplicant(BaseModel):
    pass


class Transaction(BaseModel):
    pass


class PayOnDeliveryTransaction(BaseModel):
    pass


class FundsTransferTransaction(BaseModel):
    pass


class BexTransaction(BaseModel):
    pass


class CashRegisterTransaction(BaseModel):
    pass


class CargoCompany(BaseModel):
    pass


class OrderShippingInfo(BaseModel):
    pass


class CancellationRequest(BaseModel):
    pass


class CancellationEasyReturn(BaseModel):
    pass


class CancellationReason(BaseModel):
    pass


class OrderTransaction(BaseModel):
    pass


class CancellationPlan(BaseModel):
    pass


class CancellationPlanOrderItem(BaseModel):
    pass


class DiscountItemCancellationPlan(BaseModel):
    pass


class OrderExternalStatus(BaseModel):
    pass


class VendorOrder(BaseModel):
    pass


class VendorOrderItem(BaseModel):
    pass


class Reconciliation(BaseModel):
    pass


class Invoice(BaseModel):
    pass


class PaymentInvoiceItem(BaseModel):
    pass


class InvoiceItem(BaseModel):
    pass


class Pos(BaseModel):
    pass


class Bank(BaseModel):
    pass


class CardType(BaseModel):
    pass


class Card(BaseModel):
    pass


class BinNumber(BaseModel):
    pass


class Installment(BaseModel):
    pass


class PaymentOption(BaseModel):
    pass


class BankAccount(BaseModel):
    pass


class GroupProductItem(BaseModel):
    pass


class Product(BaseModel):
    pass


class Attribute(BaseModel):
    pass


class AttributeValue(BaseModel):
    pass


class AttributeSet(BaseModel):
    pass


class AttributeConfig(BaseModel):
    pass


class ERPCategory(BaseModel):
    pass


class AttributeLanguage(BaseModel):
    pass


class ProductImage(BaseModel):
    pass


class DownloadableImage(BaseModel):
    pass


class SpecialImage(BaseModel):
    pass


class Brand(BaseModel):
    pass


class ProductVideo(BaseModel):
    pass


class BundleChapterProduct(BaseModel):
    pass


class BundleChapter(BaseModel):
    pass


class ProductCollection(BaseModel):
    pass


class ProductCollectionItem(BaseModel):
    pass


class ReportingLog(BaseModel):
    pass


class SortingAlgorithm(BaseModel):
    pass


class SortOptionAlgorithm(BaseModel):
    pass


class SortOption(BaseModel):
    pass


class ProductSortingItem(BaseModel):
    pass


class UserProfile(BaseModel):
    pass


class BEPermissionNamespace(BaseModel):
    pass


class BEPermission(BaseModel):
    pass


class FEPermissionGroup(BaseModel):
    pass


class FEPermission(BaseModel):
    pass


class CatalogGroup(BaseModel):
    pass


class ChannelGroup(BaseModel):
    pass


class BatchRequest(BaseModel):
    pass


class ContentType(BaseModel):
    pass
