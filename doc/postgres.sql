CREATE TABLE public.mqtt_data
(
    id serial NOT NULL,
    ts timestamp with time zone NOT NULL DEFAULT now(),
    topic character varying(64) NOT NULL,
    data jsonb NOT NULL,
    CONSTRAINT mqtt_data_pkey PRIMARY KEY (id)
)
    WITH (
        OIDS=FALSE
    );