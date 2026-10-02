"""What the runner needs from a harness adapter (harness-adapter.md §1).

An adapter is a module with these names. The runner looks one up by the work
order's `suites[].adapter` and calls nothing else.

Identity and capabilities
    NAME                      the adapter token, as written in `suites[].adapter`
    PRODUCER                  the `producer` object of every result it emits
    QUANTITIES                {quantity name: (native field, quantity declaration)}
    CONTEXT_KEY               the key under which harness-native facts are filed
                              in `observed_context` and `provenance.info`
    WORKLOAD_PARAMETERS       whether the order's `workload_parameters` can be applied

Driving half (harness-adapter.md §5)
    protocol(precision)       -> (applied protocol, invocation): the full protocol
                              that will apply, and what the harness is given to apply it
    locate(target_path, suite) -> the thing to run; raises Unsupported if absent
    list_cases(runnable, case_filter, env) -> the planned cases, fixed before running
    run_case(runnable, case, invocation, env, timeout, native_path) -> the run record;
                              never raises for harness failures, which become results

Translating half (harness-adapter.md §6)
    attempted(applied)        -> the repetitions the protocol asked for, the denominator
                              of `partial`
    translate(case, quantities, run, attempted) -> one output per quantity
    context_facts(native)     -> (observed context, provenance info) from native output
    harness(info)             -> the `comparison_context.harness` object
"""


class Unsupported(Exception):
    """An order this adapter cannot carry out as written; the runner refuses it."""
