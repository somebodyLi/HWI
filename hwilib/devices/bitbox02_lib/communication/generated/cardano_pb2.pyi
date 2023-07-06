"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
from . import common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CardanoNetwork:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _CardanoNetworkEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CardanoNetwork.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    CardanoMainnet: _CardanoNetwork.ValueType  # 0
    CardanoTestnet: _CardanoNetwork.ValueType  # 1
class CardanoNetwork(_CardanoNetwork, metaclass=_CardanoNetworkEnumTypeWrapper):
    pass

CardanoMainnet: CardanoNetwork.ValueType  # 0
CardanoTestnet: CardanoNetwork.ValueType  # 1
global___CardanoNetwork = CardanoNetwork


class CardanoXpubsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEYPATHS_FIELD_NUMBER: builtins.int
    @property
    def keypaths(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[common_pb2.Keypath]: ...
    def __init__(self,
        *,
        keypaths: typing.Optional[typing.Iterable[common_pb2.Keypath]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["keypaths",b"keypaths"]) -> None: ...
global___CardanoXpubsRequest = CardanoXpubsRequest

class CardanoXpubsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    XPUBS_FIELD_NUMBER: builtins.int
    @property
    def xpubs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        xpubs: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["xpubs",b"xpubs"]) -> None: ...
global___CardanoXpubsResponse = CardanoXpubsResponse

class CardanoScriptConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class PkhSkh(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYPATH_PAYMENT_FIELD_NUMBER: builtins.int
        KEYPATH_STAKE_FIELD_NUMBER: builtins.int
        @property
        def keypath_payment(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        @property
        def keypath_stake(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        def __init__(self,
            *,
            keypath_payment: typing.Optional[typing.Iterable[builtins.int]] = ...,
            keypath_stake: typing.Optional[typing.Iterable[builtins.int]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["keypath_payment",b"keypath_payment","keypath_stake",b"keypath_stake"]) -> None: ...

    PKH_SKH_FIELD_NUMBER: builtins.int
    @property
    def pkh_skh(self) -> global___CardanoScriptConfig.PkhSkh:
        """Shelley PaymentKeyHash & StakeKeyHash"""
        pass
    def __init__(self,
        *,
        pkh_skh: typing.Optional[global___CardanoScriptConfig.PkhSkh] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config",b"config","pkh_skh",b"pkh_skh"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config",b"config","pkh_skh",b"pkh_skh"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["config",b"config"]) -> typing.Optional[typing_extensions.Literal["pkh_skh"]]: ...
global___CardanoScriptConfig = CardanoScriptConfig

class CardanoAddressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NETWORK_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
    network: global___CardanoNetwork.ValueType
    display: builtins.bool
    @property
    def script_config(self) -> global___CardanoScriptConfig: ...
    def __init__(self,
        *,
        network: global___CardanoNetwork.ValueType = ...,
        display: builtins.bool = ...,
        script_config: typing.Optional[global___CardanoScriptConfig] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["script_config",b"script_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["display",b"display","network",b"network","script_config",b"script_config"]) -> None: ...
global___CardanoAddressRequest = CardanoAddressRequest

class CardanoSignTransactionRequest(google.protobuf.message.Message):
    """Max allowed transaction size is 16384 bytes according to
    https://github.com/cardano-foundation/CIPs/blob/master/CIP-0009/CIP-0009.md. Unlike with BTC, we
    can fit the whole request in RAM and don't need to stream.

    See also: https://github.com/input-output-hk/cardano-ledger-specs/blob/d0aa86ded0b973b09b629e5aa62aa1e71364d088/eras/alonzo/test-suite/cddl-files/alonzo.cddl#L50
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class Input(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYPATH_FIELD_NUMBER: builtins.int
        PREV_OUT_HASH_FIELD_NUMBER: builtins.int
        PREV_OUT_INDEX_FIELD_NUMBER: builtins.int
        @property
        def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        prev_out_hash: builtins.bytes
        prev_out_index: builtins.int
        def __init__(self,
            *,
            keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
            prev_out_hash: builtins.bytes = ...,
            prev_out_index: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["keypath",b"keypath","prev_out_hash",b"prev_out_hash","prev_out_index",b"prev_out_index"]) -> None: ...

    class AssetGroup(google.protobuf.message.Message):
        """https://github.com/input-output-hk/cardano-ledger/blob/d0aa86ded0b973b09b629e5aa62aa1e71364d088/eras/alonzo/test-suite/cddl-files/alonzo.cddl#L358"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class Token(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            ASSET_NAME_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            asset_name: builtins.bytes
            value: builtins.int
            """Number of tokens transacted of this asset."""

            def __init__(self,
                *,
                asset_name: builtins.bytes = ...,
                value: builtins.int = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["asset_name",b"asset_name","value",b"value"]) -> None: ...

        POLICY_ID_FIELD_NUMBER: builtins.int
        TOKENS_FIELD_NUMBER: builtins.int
        policy_id: builtins.bytes
        @property
        def tokens(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.AssetGroup.Token]: ...
        def __init__(self,
            *,
            policy_id: builtins.bytes = ...,
            tokens: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.AssetGroup.Token]] = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["policy_id",b"policy_id","tokens",b"tokens"]) -> None: ...

    class Output(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ENCODED_ADDRESS_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        SCRIPT_CONFIG_FIELD_NUMBER: builtins.int
        ASSET_GROUPS_FIELD_NUMBER: builtins.int
        encoded_address: typing.Text
        value: builtins.int
        @property
        def script_config(self) -> global___CardanoScriptConfig:
            """Optional. If provided, this is validated as a change output."""
            pass
        @property
        def asset_groups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.AssetGroup]: ...
        def __init__(self,
            *,
            encoded_address: typing.Text = ...,
            value: builtins.int = ...,
            script_config: typing.Optional[global___CardanoScriptConfig] = ...,
            asset_groups: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.AssetGroup]] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["script_config",b"script_config"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["asset_groups",b"asset_groups","encoded_address",b"encoded_address","script_config",b"script_config","value",b"value"]) -> None: ...

    class Certificate(google.protobuf.message.Message):
        """See https://github.com/input-output-hk/cardano-ledger-specs/blob/d0aa86ded0b973b09b629e5aa62aa1e71364d088/eras/alonzo/test-suite/cddl-files/alonzo.cddl#L150"""
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        class StakeDelegation(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            KEYPATH_FIELD_NUMBER: builtins.int
            POOL_KEYHASH_FIELD_NUMBER: builtins.int
            @property
            def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
            pool_keyhash: builtins.bytes
            def __init__(self,
                *,
                keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
                pool_keyhash: builtins.bytes = ...,
                ) -> None: ...
            def ClearField(self, field_name: typing_extensions.Literal["keypath",b"keypath","pool_keyhash",b"pool_keyhash"]) -> None: ...

        STAKE_REGISTRATION_FIELD_NUMBER: builtins.int
        STAKE_DEREGISTRATION_FIELD_NUMBER: builtins.int
        STAKE_DELEGATION_FIELD_NUMBER: builtins.int
        @property
        def stake_registration(self) -> common_pb2.Keypath: ...
        @property
        def stake_deregistration(self) -> common_pb2.Keypath: ...
        @property
        def stake_delegation(self) -> global___CardanoSignTransactionRequest.Certificate.StakeDelegation: ...
        def __init__(self,
            *,
            stake_registration: typing.Optional[common_pb2.Keypath] = ...,
            stake_deregistration: typing.Optional[common_pb2.Keypath] = ...,
            stake_delegation: typing.Optional[global___CardanoSignTransactionRequest.Certificate.StakeDelegation] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["cert",b"cert","stake_delegation",b"stake_delegation","stake_deregistration",b"stake_deregistration","stake_registration",b"stake_registration"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["cert",b"cert","stake_delegation",b"stake_delegation","stake_deregistration",b"stake_deregistration","stake_registration",b"stake_registration"]) -> None: ...
        def WhichOneof(self, oneof_group: typing_extensions.Literal["cert",b"cert"]) -> typing.Optional[typing_extensions.Literal["stake_registration","stake_deregistration","stake_delegation"]]: ...

    class Withdrawal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        KEYPATH_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        @property
        def keypath(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        value: builtins.int
        def __init__(self,
            *,
            keypath: typing.Optional[typing.Iterable[builtins.int]] = ...,
            value: builtins.int = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["keypath",b"keypath","value",b"value"]) -> None: ...

    NETWORK_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    FEE_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    CERTIFICATES_FIELD_NUMBER: builtins.int
    WITHDRAWALS_FIELD_NUMBER: builtins.int
    VALIDITY_INTERVAL_START_FIELD_NUMBER: builtins.int
    ALLOW_ZERO_TTL_FIELD_NUMBER: builtins.int
    network: global___CardanoNetwork.ValueType
    @property
    def inputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.Input]: ...
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.Output]: ...
    fee: builtins.int
    ttl: builtins.int
    @property
    def certificates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.Certificate]: ...
    @property
    def withdrawals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionRequest.Withdrawal]: ...
    validity_interval_start: builtins.int
    allow_zero_ttl: builtins.bool
    """include ttl even if it is zero"""

    def __init__(self,
        *,
        network: global___CardanoNetwork.ValueType = ...,
        inputs: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.Input]] = ...,
        outputs: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.Output]] = ...,
        fee: builtins.int = ...,
        ttl: builtins.int = ...,
        certificates: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.Certificate]] = ...,
        withdrawals: typing.Optional[typing.Iterable[global___CardanoSignTransactionRequest.Withdrawal]] = ...,
        validity_interval_start: builtins.int = ...,
        allow_zero_ttl: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_zero_ttl",b"allow_zero_ttl","certificates",b"certificates","fee",b"fee","inputs",b"inputs","network",b"network","outputs",b"outputs","ttl",b"ttl","validity_interval_start",b"validity_interval_start","withdrawals",b"withdrawals"]) -> None: ...
global___CardanoSignTransactionRequest = CardanoSignTransactionRequest

class CardanoSignTransactionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    class ShelleyWitness(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        PUBLIC_KEY_FIELD_NUMBER: builtins.int
        SIGNATURE_FIELD_NUMBER: builtins.int
        public_key: builtins.bytes
        signature: builtins.bytes
        def __init__(self,
            *,
            public_key: builtins.bytes = ...,
            signature: builtins.bytes = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["public_key",b"public_key","signature",b"signature"]) -> None: ...

    SHELLEY_WITNESSES_FIELD_NUMBER: builtins.int
    @property
    def shelley_witnesses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CardanoSignTransactionResponse.ShelleyWitness]: ...
    def __init__(self,
        *,
        shelley_witnesses: typing.Optional[typing.Iterable[global___CardanoSignTransactionResponse.ShelleyWitness]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["shelley_witnesses",b"shelley_witnesses"]) -> None: ...
global___CardanoSignTransactionResponse = CardanoSignTransactionResponse

class CardanoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    XPUBS_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    SIGN_TRANSACTION_FIELD_NUMBER: builtins.int
    @property
    def xpubs(self) -> global___CardanoXpubsRequest: ...
    @property
    def address(self) -> global___CardanoAddressRequest: ...
    @property
    def sign_transaction(self) -> global___CardanoSignTransactionRequest: ...
    def __init__(self,
        *,
        xpubs: typing.Optional[global___CardanoXpubsRequest] = ...,
        address: typing.Optional[global___CardanoAddressRequest] = ...,
        sign_transaction: typing.Optional[global___CardanoSignTransactionRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["address",b"address","request",b"request","sign_transaction",b"sign_transaction","xpubs",b"xpubs"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","request",b"request","sign_transaction",b"sign_transaction","xpubs",b"xpubs"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["request",b"request"]) -> typing.Optional[typing_extensions.Literal["xpubs","address","sign_transaction"]]: ...
global___CardanoRequest = CardanoRequest

class CardanoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    XPUBS_FIELD_NUMBER: builtins.int
    PUB_FIELD_NUMBER: builtins.int
    SIGN_TRANSACTION_FIELD_NUMBER: builtins.int
    @property
    def xpubs(self) -> global___CardanoXpubsResponse: ...
    @property
    def pub(self) -> common_pb2.PubResponse: ...
    @property
    def sign_transaction(self) -> global___CardanoSignTransactionResponse: ...
    def __init__(self,
        *,
        xpubs: typing.Optional[global___CardanoXpubsResponse] = ...,
        pub: typing.Optional[common_pb2.PubResponse] = ...,
        sign_transaction: typing.Optional[global___CardanoSignTransactionResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["pub",b"pub","response",b"response","sign_transaction",b"sign_transaction","xpubs",b"xpubs"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["pub",b"pub","response",b"response","sign_transaction",b"sign_transaction","xpubs",b"xpubs"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["response",b"response"]) -> typing.Optional[typing_extensions.Literal["xpubs","pub","sign_transaction"]]: ...
global___CardanoResponse = CardanoResponse
